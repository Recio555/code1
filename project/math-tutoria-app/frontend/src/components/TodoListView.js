import React from 'react'
import UserCard from './User';
import TodoItem from './Todo';


export default function TodoView(props) {
    return (
        <div>
            <ul>
               <TodoItem user={props.user} />
                 {/*<UserCard user={props.user} />*/}

            </ul>
        </div>
    )
}