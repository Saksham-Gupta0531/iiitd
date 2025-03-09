import React from 'react'
import './Content.css';
import mainvideo from '../Video/mainvideo.webm';
import { useNavigate } from 'react-router-dom';

export const Content = () => {
    const navigate = useNavigate(); 
    return (

        <div className="contentmain">

            <div className="left">
                <div className="head">
                    <span>Wherever there’s <br /> data, there’s </span>
                    <span>power</span>
                </div>
                <div className="sub-head">
                    <span>
                    Logo® helps you use your data to solve<br /> problems, meet new objectives, and address <br />critical business needs. It all starts here. With <br /> the industry leader in data integration and <br /> analytics solutions that support your AI strategy.
                    </span>
                </div>
                <div className="btn">
                    <button onClick={() => navigate('/create')}>
                        Get Started
                    </button>
                </div>
            </div>
            <div className="right">
                <video autoPlay playsInline loop muted>
                    <source src={mainvideo} width={100} height={100}></source>
                </video>
            </div>

        </div>
    )
}
