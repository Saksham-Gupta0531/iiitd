import React from 'react'
import './Navbar.css'
import { useNavigate } from 'react-router-dom';

export const Navbar = () => {
    const navigate = useNavigate(); 
    return (

        <div className="navmain">
            <div className="left">
                <div className='logo'>LOG0</div>
                <div className="item">
                    <div className="left-1">Home</div>
                    <div className="left-1">AI Based</div>
                    <div className="left-1">Query Based</div>
                    <div className="left-1">Analysis</div>
                </div>
            </div>
            <div className="right">
                <div className="item">
                    <div className='right1'>Contact</div>
                    <div className='right2' onClick={() => navigate('/create')}>Get Started</div>
                </div>

            </div>
        </div>

    )
}
