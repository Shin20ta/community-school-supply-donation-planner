# Test Cases

This document records the main test cases used to verify Version 1.1 of the Community School Supply Donation Planner.

---

## Test Case 1 — Basic Package

### Input

- Project Name: Donation
- Number of Students: 20
- Total Donation Budget: $500
- Package Selection: 1 — Basic

### Expected Result

- Cost Per Student: $6
- Total Donation Cost: $120
- Money Remaining: $380
- The donation should be fully funded.

### Actual Result

- Cost Per Student: $6
- Total Donation Cost: $120
- Money Remaining: $380
- The program reported that the donation was fully funded.

### Status

**Passed**

---

## Test Case 2 — Standard Package

### Input

- Project Name: 2027 Back-To-School School Supplies Donation
- Number of Students: 20
- Total Donation Budget: $500
- Package Selection: 2 — Standard

### Expected Result

- Cost Per Student: $25
- Total Donation Cost: $500
- Money Remaining: $0
- The donation should be fully funded with no money remaining.

### Actual Result

- Cost Per Student: $25
- Total Donation Cost: $500
- Money Remaining: $0
- The program reported that the donation was fully funded with no money remaining.

### Status

**Passed**

---

## Test Case 3 — Expanded Package

### Input

- Project Name: Donation
- Number of Students: 20
- Total Donation Budget: $500
- Package Selection: 3 — Expanded

### Expected Result

- Cost Per Student: $41
- Total Donation Cost: $820
- Additional Money Needed: $320
- The program should report that the current budget is not enough.

### Actual Result

- Cost Per Student: $41
- Total Donation Cost: $820
- Additional Money Needed: $320
- The program correctly reported that more funding was needed.

### Status

**Passed**

---

## Test Case 4 — Zero Students

### Input

- Project Name: Donation
- Number of Students: 0

### Expected Result

The program should stop before asking for the budget or package and display:

`The number of students must be greater than zero.`

### Actual Result

The program displayed the correct validation message and stopped safely.

### Status

**Passed**

---

## Test Case 5 — Invalid Package Selection

### Input

- Project Name: Donation
- Number of Students: 20
- Total Donation Budget: $500
- Package Selection: 0

### Expected Result

The program should display:

`Invalid package selection.`

### Actual Result

The program displayed the correct invalid-package message.

### Status

**Passed**

---

## Testing Summary

All five primary test cases passed successfully.

The testing confirmed that the program can:

- Calculate the Basic Package correctly
- Calculate the Standard Package correctly
- Calculate the Expanded Package correctly
- Reject a zero-student entry
- Reject an invalid package selection
- Report money remaining
- Report additional money needed
- Avoid division by zero
