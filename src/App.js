import React from 'react';
import logo from './logo.svg';
import {Navbar, Button} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

let flag = false;
let dot_flag = false;
let prevX = 0;
let prevY = 0;
let currX = 0;
let currY = 0;

function App() {
  return (
  <>
  <Navbar bg="dark" variant="dark">
    <Navbar.Brand href="#home">
      <img
        alt=""
        src={logo}
        width="30"
        height="30"
        className="d-inline-block align-top"
      />{' '}
      Pictionary!
    </Navbar.Brand>
  </Navbar>
  <DrawCanvas/>
  <Button 
  variant="dark"
  className = "ClearButton"
  onClick = {erase}
  >Clear
  </Button>
  </>
  );
}


function erase() {
  let canva = document.getElementsByClassName('TheCanvas')[0];
  let ctx = canva.getContext('2d');
  ctx.clearRect(0, 0, canva.width, canva.height);
}


class DrawCanvas extends React.Component {
  componentDidMount() {
    const canvas = this.refs.canvas;
    const ctx = canvas.getContext("2d");

    canvas.addEventListener("mousemove", function (e) {
        findxy('move', e, canvas)
    }, false);
    canvas.addEventListener("mousedown", function (e) {
        findxy('down', e, canvas)
    }, false);
    canvas.addEventListener("mouseup", function (e) {
        findxy('up', e, canvas)
    }, false);
    canvas.addEventListener("mouseout", function (e) {
        findxy('out', e, canvas)
    }, false);
    
  }

  render() {
    return(
      <div>
        <canvas className="TheCanvas" ref="canvas" width={960} height={540} />
      </div>
    )
  }
}


function findxy(res, e, canvas) {
    const ctx = canvas.getContext("2d");    
    if (res == 'down') {
        prevX = currX;
        prevY = currY;
        currX = e.clientX - canvas.offsetLeft;
        currY = e.clientY - canvas.offsetTop;

        flag = true;
        dot_flag = true;
        if (dot_flag) {
            ctx.beginPath();
            ctx.fillStyle = "black";
            ctx.fillRect(currX, currY, 2, 2);
            ctx.closePath();
            dot_flag = false;
        }
    }
    if (res == 'up' || res == "out") {
        flag = false;
    }
    if (res == 'move') {
        if (flag) {
            prevX = currX;
            prevY = currY;
            currX = e.clientX - canvas.offsetLeft;
            currY = e.clientY - canvas.offsetTop;
            draw(ctx);
        }
    }
}

function draw(ctx) {
    ctx.beginPath();
    ctx.moveTo(prevX, prevY);
    ctx.lineTo(currX, currY);
    ctx.strokeStyle = "black";
    ctx.lineWidth = 3;
    ctx.stroke();
    ctx.closePath();
}


export default App;