#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 22:17:31 2026

@author: siyasrivastava
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>A Valentine Awakens</title>

    <style>
        body {
            margin: 0;
            background: black;
            color: #ffe81f;
            font-family: 'Arial', sans-serif;
            overflow: hidden;
            text-align: center;
        }

        /* STARFIELD */
        body::before {
            content: "";
            position: fixed;
            width: 100%;
            height: 100%;
            background: radial-gradient(white 1px, transparent 1px),
                        radial-gradient(white 1px, transparent 1px);
            background-size: 3px 3px;
            background-position: 0 0, 1.5px 1.5px;
            opacity: 0.4;
            z-index: -1;
        }

        h1 {
            font-size: 40px;
        }

        /* INTRO CRAWL */
        #intro {
            perspective: 400px;
            height: 100vh;
            overflow: hidden;
        }

        .crawl {
            font-size: 28px;
            width: 80%;
            margin: auto;
            transform-origin: 50% 100%;
            animation: crawl 15s linear forwards;
        }

        @keyframes crawl {
            from {
                transform: rotateX(20deg) translateY(100%);
            }
            to {
                transform: rotateX(25deg) translateY(-200%);
            }
        }

        #startBtn {
            background: none;
            border: 2px solid #ffe81f;
            color: #ffe81f;
            font-size: 22px;
            padding: 12px 30px;
            border-radius: 20px;
            cursor: pointer;
            margin-top: 20px;
        }

        #main {
            display: none;
            margin-top: 120px;
        }

        /* LIGHTSABER BUTTONS */
        .yes {
            background: red;
            color: white;
            box-shadow: 0 0 20px red;
        }

        .no {
            background: blue;
            color: white;
            box-shadow: 0 0 20px blue;
            position: absolute;
        }

        button {
            font-size: 22px;
            padding: 15px 35px;
            border-radius: 25px;
            border: none;
            cursor: pointer;
            margin: 20px;
        }

        /* FORCE HEARTS */
        .heart {
            position: fixed;
            top: -10px;
            font-size: 22px;
            animation: fall linear infinite;
            color: red;
            text-shadow: 0 0 10px red;
        }

        @keyframes fall {
            to {
                transform: translateY(110vh);
            }
        }
    </style>
</head>

<body>

    <!-- INTRO -->
    <div id="intro">
        <div class="crawl">
            <p>Episode ❤️</p>
            <p>A VALENTINE AWAKENS</p>
            <p>
            In a galaxy not so far away,  
            one brave soul has gathered the courage  
            to ask a very important question...
            </p>
            <button id="startBtn" onclick="start()">Begin Mission</button>
        </div>
    </div>

    <!-- MAIN -->
    <div id="main">
        <h1>Will you be my Valentine? 💫</h1>

        <button class="yes" onclick="yes()">Yes ❤️</button>
        <button class="no" id="no" onmouseover="move()">No 💙</button>
    </div>

    <!-- SOUNDS -->
    <audio id="yesSound">
        <source src="https://www.soundjay.com/button/sounds/button-3.mp3">
    </audio>

    <audio id="noSound">
        <source src="https://www.soundjay.com/button/sounds/button-10.mp3">
    </audio>

    <script>
        let speed = 300;

        function start() {
            document.getElementById("intro").style.display = "none";
            document.getElementById("main").style.display = "block";
        }

        function yes() {
            document.getElementById("yesSound").play();
            document.body.innerHTML =
            "<h1>The Force is Strong With Us 💖✨</h1>";
        }

        function move() {
            const b = document.getElementById("no");
            document.getElementById("noSound").play();

            speed += 200;
            const x = Math.random() * (window.innerWidth - b.offsetWidth);
            const y = Math.random() * (window.innerHeight - b.offsetHeight);

            b.style.transition = speed / 1000 + "s";
            b.style.left = x + "px";
            b.style.top = y + "px";
        }

        function createHeart() {
            const heart = document.createElement("div");
            heart.className = "heart";
            heart.innerHTML = "❤️";
            heart.style.left = Math.random() * 100 + "vw";
            heart.style.animationDuration = (2 + Math.random() * 3) + "s";
            document.body.appendChild(heart);

            setTimeout(() => heart.remove(), 5000);
        }

        setInterval(createHeart, 300);
    </script>

</body>
</html>
"""

if __name__ == "__main__":
    app.run()


