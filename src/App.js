import React from 'react';
import logo from './logo.svg';
import {Navbar, Nav, Button} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import HowToPlay from './HowToPlay'

// Variables for the drawing application
let flag = false;
let dot_flag = false;
let prevX = 0;
let prevY = 0;
let currX = 0;
let currY = 0;

//  the object to be drawn
let toDraw;
// the timer id of the interval 
let timerID;
// a boolean value checking if drawing has begun
let startedDrawing = false;
// game is in progress
let gameinProgress = true;

function App() {
  return (
  <>
  <Router>
  <Navbar bg="dark" variant="dark">
    <Navbar.Brand href="/">
      <img
        alt=""
        src={logo}
        width="30"
        height="30"
        className="d-inline-block align-top"
      />{' '}
      Pictionary!
    </Navbar.Brand>
    <Link className="nav-link whitelink" to="/how2play" pullRight>How to Play</Link>
    <Link className="ml-auto nav-link whitelink" to="/old_drawings">Older drawings</Link>
    <Nav.Link className="whitelink" pullRight>
    Login
    </Nav.Link>
  </Navbar>
    <Route exact path="/how2play">
      <HowToPlay />
    </Route>
    <Route exact path="/">
      <Home />
    </Route>
  </Router>
  </>
  );
}

function Home() {
  return (
    <>
  <DrawBox/>
  <DrawCanvas/>
  <PredBox/>
  <Button 
  variant="dark"
  size="lg"
  className = "ClearButton"
  onClick = {erase}
  >Clear
  </Button>
  <Button 
  variant="dark"
  size="lg"
  className = "NewGameBUtton"
  onClick = {newGame}
  >New Game
  </Button> 
    </>
  );
}


// Clears the canvas for redrawing
function erase() {
  let canvas = document.getElementsByClassName('TheCanvas')[0];
  let ctx = canvas.getContext('2d');
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle  = "white";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
}

// takes a picture of the canvas and sends it for processing
function saveCanvas() {
  let canvas = document.getElementsByClassName('TheCanvas')[0];
  canvas.toBlob(
  function(blob) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (this.readyState === 4 && this.status === 200 ) {
        let response = xhr.responseText;
        displayPrediction(response);
        console.log(response);
      }
    }
    xhr.open('POST', '/api/canvas_img',true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.send(blob);
  },
  'image/jpeg',1.0);
}

function newGame() {
  erase();
  let predBox = document.getElementsByClassName('PredBox')[0];
  predBox.innerText = "";
  whatToDraw();
  gameinProgress = true;
}

// displays the prediction of the neural net
function displayPrediction(prediction) {
  let predBox = document.getElementsByClassName('PredBox')[0];
  predBox.innerText = "I see : " + prediction;
  if(prediction === toDraw) {
    gameOver();

  }
}

function gameOver() {
  let predEle = document.getElementsByClassName('PredBox')[0];
  predEle.innerText = "Well drawn!";
  console.log("Game over.");

  // reset state
  clearInterval(timerID);
  startedDrawing = false;

  //disable drawing
  gameinProgress = false;
}

// fetches the object to be drawn
function whatToDraw() {
    let divEle = document.getElementsByClassName('DrawBox')[0];
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (this.readyState === 4 && this.status === 200 ) {
        toDraw = xhr.responseText;
        divEle.innerText =  'Draw : ' + toDraw;
      }
    }
    xhr.open('GET', '/api/object_name',true);
    xhr.send();
}

// Submission throttling starts only after the user has started drawing
function setBoolInterval() {
  if(startedDrawing == false) {
    startedDrawing = true;
    timerID = setInterval(saveCanvas,2000);
  }
}

class DrawBox extends React.Component {
  componentDidMount() {
    whatToDraw();
  }

  render() {
    return(
      <div className="DrawBox">
      </div> //ignore comment
      )
  }
}

class PredBox extends React.Component {
  render() {
    return(
      <div className="PredBox">
      </div> //ignore comment
    )
  }
}

// canvas component
class DrawCanvas extends React.Component {
  componentDidMount() {
    const canvas = this.refs.canvas;

    canvas.addEventListener("mousemove", function (e) {
        if (gameinProgress) {
          findxy('move', e, canvas)          
        }
    }, false);
    canvas.addEventListener("mousedown", function (e) {
        if (gameinProgress) {
          setBoolInterval()
          findxy('down', e, canvas)
        }
    }, false);
    canvas.addEventListener("mouseup", function (e) {
        if (gameinProgress) {
          findxy('up', e, canvas);
          saveCanvas();
        }
    }, false);
    canvas.addEventListener("mouseout", function (e) {
        if (gameinProgress) {
          findxy('move', e, canvas)          
        }
    }, false);
    
    const ctx = canvas.getContext("2d");    
    ctx.fillStyle  = "white";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
  }

  render() {
    return(
      <div>
        <canvas className="TheCanvas" ref="canvas" width={960} height={540} />
      </div> //ignore comment
    )
  }
}

function findxy(res, e, canvas) {
    const ctx = canvas.getContext("2d");    
    if (res === 'down') {
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
    if (res === 'up' || res === "out") {
        flag = false;
    }
    if (res === 'move') {
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