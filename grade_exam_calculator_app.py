<!DOCTYPE html>
 <html lang="en">
 <head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>Grade Calculator</title>
 <!-- Include PyScript-->
 <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
 <script defer src="https://pyscript.net/latest/pyscript.js"></script>
 <style>
 body {
 margin: 0;
 padding: 0;
 font-family: 'Verdana', sans-serif;
 background-color: #003b46; /* Dark blue-green background */
 color: #e0f7fa; /* Light cyan text for contrast */
 display: flex;
 justify-content: center;
 align-items: center;
 height: 100px;
 overflow: hidden;
 }
 .container {
 background-color: #004d40; /* Dark teal for the container */
 border-radius: 8px; /* Rounded corners */
 box-shadow: 0 4px 8px rgba(0, 0, 0, 0.7); /* Dark shadow */
 padding: 30px;
 width: 100%;
 max-width: 400px;
 text-align: center;
 animation: fadeIn 1s ease-out;
 }
 @keyframes fadeIn {
 from { opacity: 0; transform: translateY(10px); }
 to { opacity: 1; transform: translateY(0); }
 }
 h1 {
 color: #00acc1; /* Bright cyan accent color */
 font-size: 24px;
 margin-bottom: 15px;
 font-weight: 700;
 animation: bounceIn 1s ease-out;
 }
 @keyframes bounceIn {
0%{ transform: scale(0.8); opacity: 0; }
 50% { transform: scale(1.1); opacity: 1; }
 100% { transform: scale(1); }
 }
 input[type="number"],
 button {
 width: 100%;
 padding: 12px;
 margin: 10px 0;
 border-radius: 6px;
 border: 1px solid #004d40; /* Dark teal border */
 font-size: 16px;
 font-weight: bold;
 box-sizing: border-box;
 transition: all 0.3s ease;
 }
 input[type="number"] {
 background-color: #004d40; /* Dark teal input background */
 color: #e0f7fa; /* Light text in input */
 }
 button {
 background-color: #00bcd4; /* Bright cyan button background */
 color: #003b46; /* Dark blue-green text on button */
 cursor: pointer;
 border: none;
 }
 button:hover {
 background-color: #00acc1; /* Slightly darker cyan on hover */
 transform: translateY(-2px);
 box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
 }
 .modal {
 display: none;
 position: fixed;
 z-index: 1000;
 left: 0;
 top: 0;
 width: 100%;
 height: 100%;
 overflow: auto;
 background-color: rgba(0, 0, 0, 0.8); /* Darker overlay */
 }
.modal-content {
 background-color: #004d40; /* Dark teal for modal */
 margin: 10% auto;
 padding: 20px;
 border-radius: 8px;
 width: 80%;
 max-width: 400px;
 animation: fadeIn 0.5s ease-out;
 }
 .modal-header,
 .modal-footer {
 border-bottom: 1px solid #003b46; /* Darker border for header and footer */
 padding: 10px 0;
 }
 .modal-footer {
 border-top: 1px solid #003b46; /* Darker border for footer */
 text-align: right;
 }
 .modal-header h2 {
 margin: 0;
 color: #00bcd4; /* Bright cyan for modal header */
 font-size: 22px;
 }
 .close {
 color: #e0f7fa;
 float: right;
 font-size: 28px;
 font-weight: bold;
 }
 .close:hover,
 .close:focus {
 color: #00acc1; /* Bright cyan on hover */
 text-decoration: none;
 cursor: pointer;
 }
 .message {
 margin: 10px 0;
 transition: opacity 0.5s ease;
 }
 .error {
 color: #e57373; /* Light red for error messages */
font-weight: 600;
 }
 .logo {
 color: #e0f7fa;
 padding: 10px 20px;
 display: inline-block;
 box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5); /* Darker shadow */
 }
 .logo-text {
 font-size: 48px; /* Adjust size as needed */
 font-weight: bold;
 color: #e0f7fa; /* Light text for the logo */
 }
 .calculator {
 color: #e0f7fa; /* Light text color */
 }
 </style>
 </head>
 <body>
 <div class="logo">
 <span class="logo-text">Grade<span class="calculator">Calculator</span></span>
 <input type="number" id="absences" placeholder="Enter Number of Absences" min="0"
 step="1">
 <input type="number" id="prelimExam" placeholder="Enter Prelim Exam Grade
 (0-100)" min="0" max="100" step="0.01">
 <input type="number" id="quizzes" placeholder="Enter Quizzes Grade (0-100)" min="0"
 max="100" step="0.01">
 <input type="number" id="requirements" placeholder="Enter Requirements Grade
 (0-100)" min="0" max="100" step="0.01">
 <input type="number" id="recitation" placeholder="Enter Recitation Grade (0-100)"
 min="0" max="100" step="0.01">
 <button id="calculateBtn">Calculate</button>
 </div>
 <!-- The Modal-->
 <div id="resultModal" class="modal">
 <div class="modal-content">
 <div class="modal-header">
 <span class="close" id="closeModal">&times;</span>
 <h2>Calculation Results</h2>
 </div>
 <div class="modal-body">
<p><b>Prelim Grade:</b> <span id="prelimGrade"></span></p>
 <p><b>To pass with 75%, you need a Midterm grade of</b>
 <span id="midtermGrade"></span><b> and a Final grade of</b> <span
 id="finalGrade"></span></p>
 <p><b>To achieve 90%, you need a Midterm grade of</b> <span
 id="midtermGrade2"></span><b> and a Final grade of</b> <span
 id="finalGrade2"></span></p>
 <p id="passMessage" class="message"></p>
 <p id="errorMessage" class="error"></p>
 </div>
 <div class="modal-footer">
 <button id="closeModalBtn">Close</button>
 </div>
 </div>
 </div>
 <py-script>
 from pyscript import Element
 async def calculate_grade(event):
 # Hide previous results and clear messages
 result_element = Element("resultModal").element
 result_element.style.display = "none"
 Element("prelimGrade").element.innerHTML = "N/A"
 Element("midtermGrade").element.innerHTML = "N/A"
 Element("finalGrade").element.innerHTML = "N/A"
 Element("midtermGrade2").element.innerHTML = "N/A"
 Element("finalGrade2").element.innerHTML = "N/A"
 Element("passMessage").element.innerHTML = ""
 Element("errorMessage").element.innerHTML = ""
 try:
 # Retrieve input values
 absences = int(Element("absences").element.value.strip())
 prelim_exam = float(Element("prelimExam").element.value.strip())
 quizzes = float(Element("quizzes").element.value.strip())
 requirements = float(Element("requirements").element.value.strip())
 recitation = float(Element("recitation").element.value.strip())
 # Validate input ranges
 if absences < 0:
 raise ValueError("Absences cannot be negative.")
 if not (0 <= prelim_exam <= 100):
 raise ValueError("Prelim Exam Grade must be between 0 and 100.")
 if not (0 <= quizzes <= 100):
 raise ValueError("Quizzes Grade must be between 0 and 100.")
 if not (0 <= requirements <= 100):
 raise ValueError("Requirements Grade must be between 0 and 100.")
if not (0 <= recitation <= 100):
 raise ValueError("Recitation Grade must be between 0 and 100.")
 except ValueError as e:
 Element("errorMessage").element.innerHTML = str(e)
 result_element.style.display = "block"
 return
 # Attendance Calculation
 attendance = 100- (absences * 10)
 if absences >= 4:
 Element("errorMessage").element.innerHTML = "FAILED due to absences."
 result_element.style.display = "block"
 return
 # Class Standing Calculation
 class_standing = (0.40 * quizzes) + (0.30 * requirements) + (0.30 * recitation)
 # Prelim Grade Calculation
 prelim_grade = (0.60 * prelim_exam) + (0.10 * attendance) + (0.30 * class_standing)
 # Required Midterm and Final Grades
 prelim_percent = 0.20
 midterm_percent = 0.30
 final_percent = 0.50
 passing_grade = 75
 passing_grade2 = 90 # Dean's Lister Grade
 current_total = prelim_grade * prelim_percent
 required_total = passing_grade- current_total
 required_total2 = passing_grade2- current_total
 # Midterm/Final Grades for 75 Passing
 if required_total > 0:
 required_midterm_and_final = required_total / (midterm_percent + final_percent)
 else:
 required_midterm_and_final = 0
 # Midterm/Final Grades for 90 Passing (Dean's Lister)
 if required_total2 > 0:
 required_midterm_and_final2 = required_total2 / (midterm_percent +
 final_percent)
 else:
 required_midterm_and_final2 = 0
 # Update UI with results
 Element("prelimGrade").element.innerHTML = f"{prelim_grade:.2f}%"
Element("midtermGrade").element.innerHTML =
 f"{required_midterm_and_final:.2f}%"
 Element("finalGrade").element.innerHTML = f"{required_midterm_and_final:.2f}%"
 Element("midtermGrade2").element.innerHTML =
 f"{required_midterm_and_final2:.2f}%"
 Element("finalGrade2").element.innerHTML = f"{required_midterm_and_final2:.2f}%"
 # Display modal
 result_element.style.display = "block"
 # Bind event to button click
 Element("calculateBtn").element.onclick = calculate_grade
 # Modal close functionality
 def close_modal(event):
 Element("resultModal").element.style.display = "none"
 Element("closeModal").element.onclick = close_modal
 Element("closeModalBtn").element.onclick = close_modal
 </py-script>
 </body>
 </html>
