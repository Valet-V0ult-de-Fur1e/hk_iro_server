/* eslint-disable jsx-a11y/alt-text */
import React from "react";
import { Nav, NavLink, NavMenu } from "./NavbarElements";
  
const Navbar = () => {
  return (
    <>
      <Nav>
        <img src='headimg.png'/>
        <NavMenu>    
          <NavLink to="/" activeStyle>
            Главная страница
          </NavLink>
          <NavLink to="/blogs" activeStyle>
            Форма
          </NavLink>
          <NavLink to="/sign-up" activeStyle>
            Зарегистрироваться
          </NavLink>
        </NavMenu>
      </Nav>
    </>
  );
};
  
export default Navbar;