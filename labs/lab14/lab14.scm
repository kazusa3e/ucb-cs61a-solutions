(define (split-at lst n) (
    cond
        ((> n (length lst)) (cons lst nil))
        ((= n 0) (cons nil lst))
        (else (
            let (
                (new (split-at (cdr lst) (- n 1)))
            )
                (cons
                    (append (list (car lst)) (car new))
                    (cdr new)
                )
        ))
))

; Tree Abstraction
; Constructs tree given label and list of branches
(define (tree label branches)
  (cons label branches))

; Returns the label of the tree
(define (label t) (car t))

; Returns the list of branches of the given tree
(define (branches t) (cdr t))

; Returns #t if t is a leaf, #f otherwise
(define (is-leaf t) (null? (branches t)))

(define (filter-odd t) (
    if (is-leaf t)
        (tree (if (even? (label t)) nil (label t)) nil)
        (tree
            (if (even? (label t)) nil (label t))
            (map filter-odd (branches t))
        )
))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (swap expr) (
    let (
        (oper (car expr))
        (first (cadr expr))
        (second (caddr expr))
        (rest (cdr (cdr (cdr expr))))
    )
        (if (> (eval second) (eval first))
            (append (list oper second first) rest)
            expr
        )
))
