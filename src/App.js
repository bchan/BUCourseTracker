import React from 'react';
// import logo from './logo.svg';
import boston_terrier from './boston_terrier.png'
import './App.css';
import NavBar from "./NavBar";
import { Link } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <NavBar/>
      <header className="App-header">
        {/* <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p> */}
        
        <p>
          <img src={boston_terrier} className="App-logo" alt="logo"/>
          <br />
          Didn't get into a class? <a className="App-link">Track</a> it now!
          <br />
          <Link className="App-link" to="/signIn">Log in</Link> or <a className="App-link">sign up</a> to get started.
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
