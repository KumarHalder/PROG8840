import React from "react";
import DataDisplay from "./DisplayData";

const App = () => {
  return (
    <div
      style={{
        display: "flex",
        justifyContent: "center",
        flexDirection: "column",
        padding: "100px",
      }}
    >
      <h1>My Book App</h1>
      <DataDisplay />
    </div>
  );
};

export default App;
