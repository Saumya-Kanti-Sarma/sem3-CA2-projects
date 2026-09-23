/* eslint-disable react-hooks/set-state-in-effect */
import { useEffect, useState } from "react";
import "./App.css";

const API_URL = "http://localhost:5000/employees";

function App() {
  const [employees, setEmployees] = useState([]);
  const [form, setForm] = useState({
    name: "",
    email: "",
    department: "",
    salary: ""
  });

  const [editingId, setEditingId] = useState(null);


  const fetchEmployees = async () => {
    try {
      const response = await fetch(API_URL);
      console.log(response)
      const data = await response.json();
      setEmployees(data);
    } catch (error) {
      console.error("Error fetching employees:", error);
    }
  };

  useEffect(() => {
    fetchEmployees();
  }, []);

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      if (editingId) {
        const response = await fetch(`${API_URL}/${editingId}`, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            name: form.name,
            email: form.email,
            department: form.department,
            salary: Number(form.salary)
          })
        });

        const data = await response.json();

        if (!response.ok) {
          alert(data.error || "Failed to update employee");
          return;
        }

        alert("Employee updated successfully");

      } else {
        // CREATE
        const response = await fetch(API_URL, {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            name: form.name,
            email: form.email,
            department: form.department,
            salary: Number(form.salary)
          })
        });

        const data = await response.json();

        if (!response.ok) {
          alert(data.error || "Failed to create employee");
          return;
        }

        alert(`Employee created with ID: ${data.employee_id}`);
      }

      // Reset form
      setForm({
        name: "",
        email: "",
        department: "",
        salary: ""
      });

      setEditingId(null);

      fetchEmployees();

    } catch (error) {
      console.error(error);
    }
  };

  // EDIT

  const handleEdit = (employee) => {
    setEditingId(employee.EMPLOYEE_ID);

    setForm({
      name: employee.NAME,
      email: employee.EMAIL,
      department: employee.DEPARTMENT,
      salary: employee.SALARY
    });
  };

  // DELETE

  const handleDelete = async (id) => {
    const confirmDelete = window.confirm(
      "Are you sure you want to delete this employee?"
    );

    if (!confirmDelete) return;

    try {
      const response = await fetch(`${API_URL}/${id}`, {
        method: "DELETE"
      });

      const data = await response.json();

      if (!response.ok) {
        alert(data.error || "Failed to delete employee");
        return;
      }

      alert("Employee deleted successfully");

      fetchEmployees();

    } catch (error) {
      console.error(error);
    }
  };

  // CANCEL EDIT

  const cancelEdit = () => {
    setEditingId(null);

    setForm({
      name: "",
      email: "",
      department: "",
      salary: ""
    });
  };

  return (
    <div className="container">

      <h2>Open Narrator Employee Management System</h2>

      {/* FORM */}

      <form onSubmit={handleSubmit} className="employee-form">

        <input
          type="text"
          name="name"
          placeholder="Name"
          value={form.name}
          onChange={handleChange}
          required
        />

        <input
          type="email"
          name="email"
          placeholder="Email"
          value={form.email}
          onChange={handleChange}
          required
        />

        <input
          type="text"
          name="department"
          placeholder="Department"
          value={form.department}
          onChange={handleChange}
        />

        <input
          type="number"
          name="salary"
          placeholder="Salary"
          value={form.salary}
          onChange={handleChange}
        />

        <button type="submit">
          {editingId ? "Update Employee" : "Add Employee"}
        </button>

        {editingId && (
          <button
            type="button"
            onClick={cancelEdit}
            className="cancel-button"
          >
            Cancel
          </button>
        )}

      </form>

      {/* TABLE */}

      <table>

        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Department</th>
            <th>Salary</th>
            <th>Actions</th>
          </tr>
        </thead>

        <tbody>

          {employees.map((employee) => (

            <tr key={employee.EMPLOYEE_ID}>

              <td>{employee.EMPLOYEE_ID}</td>

              <td>{employee.NAME}</td>

              <td>{employee.EMAIL}</td>

              <td>{employee.DEPARTMENT}</td>

              <td>{employee.SALARY}</td>

              <td>

                <button
                  onClick={() => handleEdit(employee)}
                >
                  Edit
                </button>

                <button
                  onClick={() =>
                    handleDelete(employee.EMPLOYEE_ID)
                  }
                  className="delete-button"
                >
                  Delete
                </button>

              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}

export default App;