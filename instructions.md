Instructions:
This is a simple e-commerce application that a customer can use to purchase a book, but it's missing the payments functionality — your goal is to integrate Stripe to get this application running! To help reduce the amount of configuration and time spent on this project, you can find boilerplate applications to use as starting points in Ruby, Javascript, and Python here:
https://github.com/adamjstevenson/takehome-project-ruby
https://github.com/mattmitchell6/sa-takehome-project-node 
https://github.com/marko-stripe/sa-takehome-project-python

We provide these as a starting point, but you're welcome to use whatever language and framework you’re most comfortable with. Your output should be a simple program that allows the user to take a few actions:
- Select a book to purchase.
- Checkout and purchase the item using Stripe Elements.
- Display a confirmation of purchase to the user with the total amount of the charge and Stripe Payment Intent ID (beginning with pi_).

When you're done, push the project to Github or place in a zip file and return along with a document (README.md, a Google doc, etc.) containing the following:
- How to build, configure and run your application.
- How does the solution work? Which Stripe APIs does it use? How is your application architected?
- How did you approach this problem? Which docs did you use to complete the project? What challenges did you encounter?
- How you might extend this if you were building a more robust instance of the same application.

Some tips:
- Please calibrate the quality of your submission as if you were presenting it to a customer / user.
- We would like you to use the Stripe Payment Element and not Stripe Checkout. 
- Your `readme.md` is a very important part of the submission, please carefully consider your explanation of the solution as well as your instructions on how to run your example. 
- This document will give us a chance to assess your writing abilities as well.

We'll also extend this example later in the interview process where you would be asked to present to one of our team members and add a feature to your application. We suggest your application is structured in such a way that you’re able to run it locally and integrate other Stripe features easily later.