import React, { useEffect, useState } from "react";
import { useCookies } from "react-cookie";
import axios from 'axios';
import logo from './logo.svg';
import './App.css';
import os from 'os';

const loadBackendDetails = async () => {
  const response = await axios.get('http://localhost:8000/');
  return response.data;
};

const App = () => {
  const [cookies, setCookie] = useCookies(['userId']);
  const [counter, setCounter] = useState(false);
  const [hostName, setHostName] = useState(false);
  const [userId, setUserId] = useState(false);

  if (!cookies.user) {
      setCookie("user", Date.now(), { path: '/' })
    };
  axios.defaults.headers['user'] = cookies.user;
  useEffect(() => {
    loadBackendDetails().then(response => {
      setCounter(response.counter);
      setHostName(response.hostName);
      setUserId(cookies.user);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        {userId && counter && hostName && (
          <>
            <p>
              You ({userId}) visited this site {counter} times
            </p>
            <p>
              BE hostanme: <strong>{hostName}</strong>
            </p>
            <p>
              FE hostanme: <strong>{os.hostname()}</strong>
            </p>
          </>
        )}
      </header>
    </div>
  );
}

export default App;
