import { NavLink } from 'react-router-dom';
import '../../css/Header.css';

const Header = () => {
  return (
    <header className="bg-blue-600 text-white p-4">
      <nav>
        <ul className="flex justify-end space-x-6">
          <li>
            <NavLink to="/" className="text-white hover:text-gray-300">Home</NavLink>
          </li>
          <li>
            <NavLink to="/about" className="text-white hover:text-gray-300">About</NavLink>
          </li>
          <li>
            <NavLink to="/LoginForm" className="text-white hover:text-gray-300">Login</NavLink>
           
          </li>
          
           <li>
             <NavLink to = "/loginFormPrueba" className="text-white hover:text-gray-300">log</NavLink>
          </li>
          
        </ul>
      </nav>
    </header>
  );
};

export default Header;



