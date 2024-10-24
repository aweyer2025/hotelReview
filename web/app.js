const oracledb = require('oracledb');
async function runApp()
{
  let connection;
  try {
    //change user,password,and connectionString as needed to make a connection to a different database
    connection = await oracledb.getConnection({ user: "C##aweyer", password: "Passw0rd", connectionString: "localhost:1521/FREE" });
    console.log("Successfully connected to Oracle Database");
  
 
  
    // Querying database for rating from each catagory
    const overallRating = `SELECT FROM RATING WHERE HOTEL `;
    const room = 'SELECT FROM RATING WHERE';
    const service = '';
    const cleanliness = '';
    const location = '';
    let result = await connection.executeMany(overallRating, room, service, cleanliness, location);
    console.log(result.rowsAffected, "query completed successfuly");
    connection.commit();
  




//Query that returns all the titles in the table
bookInfo = await connection.execute(
    `SELECT * FROM BOOK`, 
    [], 
    { outFormat: oracledb.OUT_FORMAT_OBJECT }
  );
  
  const rs = bookInfo.resultSet; 
  // let row;
  
  console.log(bookInfo.rows)
//Query to find data based on ISBN
let ISBN='978-0735211292';
SingleQuery = await connection.execute(
  `SELECT * FROM BOOK WHERE ISBN=:isbn`,
  [ISBN],
  { outFormat: oracledb.OUT_FORMAT_OBJECT }
);
  console.log(`"Information for the book that has ISBN of " ${ISBN} is`, SingleQuery.rows[0])
  //Error Handling
  } catch (err) {
    console.error(err);
  } finally {
    if (connection) {
      try {
        await connection.close();
      } catch (err) {
        console.error(err);
      }
    }
  }
}

runApp();