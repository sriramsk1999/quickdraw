import React from 'react';
import {Container} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import Model from "./model.png" 

function HowToPlay() {
  return (
  <>
  <Container className="how2play"> 
  <h1 style={{textAlign:"center"}}> Welcome! </h1> 
  <br/><br/><br/>
  <p>
    <b>Pictionary!</b> is a game where one player has to communicate the name of an object only with pictures and no words. We have created a simple version of the game where you play against the 
    computer. You are given an object to draw and while you're drawing, the computer tries to guess what you are attempting to draw. A neural network trained on thousands on drawings resides on the 
    server and it takes in what you have drawn as input and guesses which object you might have drawn. 
  </p>

  <p>
    The model has been trained on samples of the following objects : [] The architecture of the model is as follows:
  </p>

  <img src={Model} height={1000} style={{marginLeft:'30%',marginBottom:'20px'}}/>

  <p>
    You can also see the outcomes of your previous matches and your drawings. We hope you enjoyed this game!
  </p>
  

  </Container>
  </>
  );
}

export default HowToPlay;