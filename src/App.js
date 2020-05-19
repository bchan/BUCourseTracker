import React from 'react';
// import logo from './logo.svg';
import boston_terrier from './boston_terrier.png'
import './App.css';
import NavBar from "./NavBar";

function App() {
  return (
    <div className="App">
      <NavBar/>
      <header className="App-header">
        {/* <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p> */}
        <img src={boston_terrier} className="App-logo" />
        <p>
          Didn't get into a class? <a className="App-link">Track</a> it now!
        </p>
        {/* <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a> */}
      </header>
    </div>
  );
}

export default App;
