import React from 'react'
import './Home.css'
import { Navbar } from './Navbar'
import { Content } from './Content'
import { useNavigate } from 'react-router-dom';


export const Home = () => {
  const navigate = useNavigate(); 
  return (
    <div>
        <div className='Navbar'><Navbar /></div>
        <div className='content'><Content /></div>
    </div>
  )
}
