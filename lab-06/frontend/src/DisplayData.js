import React, { useEffect, useState } from "react";
import axios from "axios";

const DataDisplay = () => {
  const [books, setBooks] = useState([]);
  const endpoint = "https://h5lmi78xqa.execute-api.us-east-1.amazonaws.com/dev";
  useEffect(() => {
    axios
      .get(`${endpoint}/books`)
      .then((response) => {
        setBooks(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  const handleDelete = (id) => {
    axios
      .delete(`${endpoint}/books/${id}`)
      .then((response) => {
        setBooks(books.filter((book) => book.id !== id));
      })
      .catch((error) => {
        console.error(error);
      });
  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
      }}
    >
      <h1 style={{ textAlign: "center" }}>Book List</h1>
      <table border="1">
        <thead>
          <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Author</th>
          </tr>
        </thead>
        <tbody>
          {books.map((book) => (
            <tr key={book.id}>
              <td>{book.id}</td>
              <td>{book.title}</td>
              <td>{book.author}</td>
              <td>
                <button onClick={() => handleDelete(book.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default DataDisplay;
