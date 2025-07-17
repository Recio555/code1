import React from 'react';
import Button from '@mui/material/Button';
import { useState } from 'react';


export default function Hijo({padreAHijo}) {

    const dato = "Esta es la data del componente hijo."
    
    return (
        <div>
             <Button variant="contained"
              onClick={() =>padreAHijo(dato)}>Clic Hijo</Button>
             <div>
                
            <p>
                <span style={{ fontWeight: 'bold', textDecoration: 'underline' }}>
                {'user.name'}:
                </span>{' '}
                <span>{'user.item_count'}</span>
                <button onClick={() => deleteTodoHandler(user.title)}
                 className="btn btn-outline-danger my-2 mx-2" 
                 style={{'borderRadius':'50px',}}>X</button>

                <hr></hr>
            </p>
        </div>
        </div>
    );
}