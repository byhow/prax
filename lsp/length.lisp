(defun length(list)
  (cond
    ((null list) 0)
    (t (+ 1 (length(cdr list))))
  )
)
