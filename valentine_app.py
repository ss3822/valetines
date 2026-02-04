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
        <title>Valentine?</title>
        <style>
            body {
                background-color: pink;
                font-family: Arial;
                text-align: center;
                margin-top: 120px;
            }
            h1 {
                color: #b30059;
                font-size: 40px;
            }
            button {
                font-size: 22px;
                padding: 15px 30px;
                border-radius: 12px;
                border: none;
                cursor: pointer;
                margin: 20px;
            }
            #no {
                position: absolute;
            }
        </style>
    </head>

    <body>
        <h1>Will you be my Valentine? 💖</h1>

        <button onclick="yes()">Yes 💕</button>
        <button id="no" onmouseover="move()">No 💔</button>

        <script>
            function yes() {
                document.body.innerHTML =
                "<h1>YAY 💘🥰 Happy Valentine’s Day!</h1>";
            }

            function move() {
                const b = document.getElementById("no");
                b.style.left = Math.random() * 500 + "px";
                b.style.top = Math.random() * 400 + "px";
            }
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
