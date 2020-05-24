import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

import NavBar from "./NavBar";
import SignIn from "./SignIn";
import { Route, Switch, BrowserRouter as Router } from "react-router-dom";

const NotFound = () => {
    return (
        <div style={{
            position: 'absolute', left: '50%', top: '50%',
            fontSize: '32px',
            transform: 'translate(-50%, -50%)'
        }}>
            <h3>404 - Not Found</h3>
        </div>
    );
};

const routing = (
    <div style={{backgroundColor: "#282c34"}}>
    <Router>
        <NavBar />
        <Switch>
            <Route exact path="/" component={App} />
            <Route path="/signIn" component={SignIn} />
            <Route component={NotFound} />
        </Switch>
    </Router>
    </div>
)

ReactDOM.render(routing, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
