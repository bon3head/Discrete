# Policy Matrix

## Hint Level Constraints
| Situation | Maximum permitted level |
|---|---|
| Concept help | L3 |
| Homework hint, no student attempt | L3 |
| Homework hint, submitted attempt | L4 |
| Student-attempt check | L4 |
| Verification request | L3 unless student submitted their claim/work |
| Mock exam during attempt | L0: no hints, no answers |
| Mock exam after submission | L4 feedback only |
| Review/exam prep | L3 by default |

## Reference Solution Access (Appendix F)
`reference_solution` is ALLOWED **only** when:
- `mode == "mock_exam"` AND `student_attempt.provided == true`
- `task_type == "student_attempt_check"` AND `student_attempt.provided == true`

Otherwise, request for reference solution yields `POLICY_BLOCKED` with `REFERENCE_SOLUTION_PREATTEMPT_BLOCKED`.
