import express from "express";
import oracledb from "oracledb";
import dotenv from "dotenv";
import cors from "cors";

dotenv.config();
const app = express();
app.use(cors());
app.use(express.json());
const PORT = process.env.PORT || 5000;

// Oracle database configuration
const dbConfig = {
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  connectString: process.env.DB_CONNECT_STRING
};



// Test database connection
async function testConnection() {
  let connection;

  try {
    connection = await oracledb.getConnection(dbConfig);
    console.log("Connected to Oracle Database!");
    const result = await connection.execute(`SELECT 1 FROM employees`);
    console.log("Oracle DB reachable:", result.rows[0][0]);

  } catch (error) {
    console.error("Database connection failed:", error);

  } finally {
    if (connection) {
      await connection.close();
    }
  }
}

testConnection();

// CREATE EMPLOYEE
app.post("/employees", async (req, res) => {
  const {
    name,
    email,
    department,
    salary
  } = req.body;

  let connection;

  try {

    connection = await oracledb.getConnection(dbConfig);

    const result = await connection.execute(
      `INSERT INTO employees
       (name, email, department, salary)
       VALUES
       (:name, :email, :department, :salary)
       RETURNING employee_id INTO :employee_id`,
      {
        name,
        email,
        department,
        salary,

        employee_id: {
          dir: oracledb.BIND_OUT,
          type: oracledb.NUMBER
        }
      },
      {
        autoCommit: true
      }
    );

    res.status(201).json({
      message: "Employee created successfully",
      employee_id: result.outBinds.employee_id[0]
    });

  } catch (error) {

    console.error(error);

    if (error.errorNum === 1) {
      return res.status(409).json({
        error: "Email already exists"
      });
    }

    res.status(500).json({
      error: error.message
    });

  } finally {

    if (connection) {
      await connection.close();
    }
  }
});


// GET ALL EMPLOYEES
app.get("/employees", async (req, res) => {
  let connection;
  try {
    connection = await oracledb.getConnection(dbConfig);
    const result = await connection.execute(
      `SELECT
                employee_id,
                name,
                email,
                department,
                salary
             FROM employees
             ORDER BY employee_id`,
      [],
      {
        outFormat: oracledb.OUT_FORMAT_OBJECT
      }
    );
    res.json(result.rows);

  } catch (error) {
    console.error(error);
    res.status(500).json({
      error: error.message
    });

  } finally {
    if (connection) {
      await connection.close();
    }
  }
});


// GET EMPLOYEE BY ID
app.get("/employees/:id", async (req, res) => {
  const { id } = req.params;
  let connection;
  try {
    connection = await oracledb.getConnection(dbConfig);
    const result = await connection.execute(
      `SELECT
                employee_id,
                name,
                email,
                department,
                salary
             FROM employees
             WHERE employee_id = :id`,
      {
        id
      },
      {
        outFormat: oracledb.OUT_FORMAT_OBJECT
      }
    );
    if (result.rows.length === 0) {
      return res.status(404).json({
        message: "Employee not found"
      });
    }
    res.json(result.rows[0]);
  } catch (error) {
    console.error(error);
    res.status(500).json({
      error: error.message
    });
  } finally {
    if (connection) {
      await connection.close();
    }
  }
});


// UPDATE EMPLOYEE
app.put("/employees/:id", async (req, res) => {
  const { id } = req.params;
  const { name, email, department, salary } = req.body;
  let connection;
  try {
    connection = await oracledb.getConnection(dbConfig);
    const result = await connection.execute(
      `UPDATE employees
             SET
                name = :name,
                email = :email,
                department = :department,
                salary = :salary
             WHERE employee_id = :id`,
      {
        id,
        name,
        email,
        department,
        salary
      },
      {
        autoCommit: true
      }
    );

    if (result.rowsAffected === 0) {
      return res.status(404).json({
        message: "Employee not found"
      });
    }

    res.json({
      message: "Employee updated successfully"
    });

  } catch (error) {

    console.error(error);

    res.status(500).json({
      error: error.message
    });

  } finally {

    if (connection) {
      await connection.close();
    }
  }
});


// DELETE EMPLOYEE

app.delete("/employees/:id", async (req, res) => {

  const { id } = req.params;

  let connection;

  try {

    connection = await oracledb.getConnection(dbConfig);

    const result = await connection.execute(
      `DELETE FROM employees
             WHERE employee_id = :id`,
      {
        id
      },
      {
        autoCommit: true
      }
    );

    if (result.rowsAffected === 0) {
      return res.status(404).json({
        message: "Employee not found"
      });
    }

    res.json({
      message: "Employee deleted successfully"
    });

  } catch (error) {

    console.error(error);

    res.status(500).json({
      error: error.message
    });

  } finally {

    if (connection) {
      await connection.close();
    }
  }
});



app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});