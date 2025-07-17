import React from 'react'
import UserCard from './User';
import TodoItem from './Todo';
import React, { useState, useEffect } from 'react';

import TodoView from './components/TodoListView';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';


export default function TodoView(props) {

const [todoList, setTodoList] = useState([]);
const [title, setTitle] = useState('');
const [desc, setDesc] = useState('');

useEffect(() => {
  axios.get('http://localhost:8001/api/lists')
    .then(res => {
      setTodoList(res.data);
    })
    .catch(err => {
      console.error('Error fetching todos:', err);
    });
}, []);

const addTodoHandler = () => {
  if (!title || !desc) {
    alert("Por favor ingresa título y descripción");
    return;
  }

  axios.post('http://localhost:8001/api/lists/', { title, description: desc })
    .then(res => {
      setTodoList(prev => [...prev, res.data]);
      setTitle('');
      setDesc('');
    })
    .catch(err => {
      console.error('Error adding todo:', err);
    });
};

return (
    <div className="App list-group-item  justify-content-center align-items-center mx-auto" style={{"width":"400px", "backgroundColor":"white", "marginTop":"15px"}} >
      <h1 className="card text-white bg-primary mb-1" styleName="max-width: 20rem;">Task Manager</h1>
      <h6 className="card text-white bg-primary mb-3">FASTAPI - React - MongoDB</h6>
     <div className="card-body">
      <h5 className="card text-white bg-dark mb-3">Add Your Task</h5>
      <span className="card-text"> 
        <input className="mb-2 form-control titleIn" onChange={event => setTitle(event.target.value)} placeholder='Title'/> 
        <input className="mb-2 form-control desIn" onChange={event => setDesc(event.target.value)}   placeholder='Description'/>
      <button className="btn btn-outline-primary mx-2 mb-3" style={{'borderRadius':'50px',"font-weight":"bold"}}  onClick={addTodoHandler}>Add Task</button>
      </span>
      <h5 className="card text-white bg-dark mb-3">Your Tasks</h5>
      <div >
        {todoList.map((todo, index) => (<TodoView key={index} user={todo} />))}
      </div>
      </div>
      <h6 className="card text-dark bg-warning py-1 mb-0" >Copyright 2021, All rights reserved &copy;</h6>
    </div>
  );
}