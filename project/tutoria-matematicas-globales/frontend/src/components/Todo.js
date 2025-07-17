import axios from 'axios'
import React from 'react'

function TodoItem({ user }) {
    const deleteTodoHandler = (title) => {
    axios.delete(`http://localhost:8000/api/lists`)
        .then(res => console.log(res.data)) 
    }
  
    return (
        <div>
            <p>
        
                <span style={{ fontWeight: 'bold', textDecoration: 'none' }}>{user.name} : </span> {user.item_count}

                <button onClick={() => deleteTodoHandler(user.id)} className="btn btn-outline-danger my-2 mx-2" style={{'borderRadius':'50px',}}>X</button>
                
            </p>
            <hr></hr>
        </div>
    )
}

export default TodoItem;