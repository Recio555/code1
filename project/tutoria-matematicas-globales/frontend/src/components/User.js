import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
 //{todoList.map((todo, index) => (<UserCard key={index} user={todo} />))} codigo para renderizar desde

const UserCard = ({ user }) => {
      
    return (

      <div className="max-w-sm mx-auto bg-white shadow-md rounded-2xl p-4">
      <h2 className="text-xl font-semibold text-gray-800 mb-2">{user.name}</h2>
      <p className="text-gray-600"><strong>ID:</strong> {user.id}</p>
      <p className="text-gray-600"><strong>Items:</strong> {user.item_count}</p>
    </div>
  );
};

export default UserCard;