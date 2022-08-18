;; WWSD
;; scm> (define a 1)
;; a
;; scm> a
;; 1
;; scm> (define b a)
;; b
;; scm> b
;; 1
;; scm> (define c 'a)
;; c
;; scm> c
;; a

;; WWSD
;; scm> (define a (+ 1 2))
;; a
;; scm> a
;; 3
;; scm> (define b (- (+ (* 3 3) 2) 1))
;; b
;; scm> b
;; 10
;; scm> (+ a b)
;; j13
;; scm> (= (modulo b a) (quotient 5 3))j
;; #t

;; WWSD
;; scm> (if (or #t (/ 1 0)) 1 (/ 1 0))
;; 1
;; scm> ((if (< 4 3) + -) 4 100)
;; -96

;; Q1: Virahanka-Fibonacci
(define (vir-fib n) (
    cond
        ((= n 0) 0)
        ((= n 1) 1)
        (else (+
            (vir-fib (- n 2))
            (vir-fib (- n 1))
        ))
))
(expect (vir-fib 10) 55)
(expect (vir-fib 1) 1)

;; Q2: List Making
(define with-list (
    list (list 'a 'b) 'c 'd (list 'e)
))
(draw with-list)

(define with-quote
    '((a b) c d (e))
)
(draw with-quote)

(define helpful-list
   (cons 'a (cons 'b nil)))
(draw helpful-list)

(define another-helpful-list
    (cons 'c (cons 'd (cons (cons 'e nil) nil))))
(draw another-helpful-list)

(define with-cons
    (cons
        helpful-list another-helpful-list
    )
)
(draw with-cons)

;; Q3: List Concatenation
(define (list-concat a b) (
    cond
        ((null? a) b)
        (else (cons
            (car a)
            (list-concat (cdr a) b)
        ))
))

(expect (list-concat '(1 2 3) '(2 3 4)) (1 2 3 2 3 4))
(expect (list-concat '(3) '(2 1 0)) (3 2 1 0))

;; Q4: Map
(define (map-fn fn lst) (
    if (null? lst) lst (
        cons (fn (car lst)) (map-fn fn (cdr lst))
    )
))

(map-fn (lambda (x) (* x x)) '(1 2 3))
; expect (1 4 9)

;; Q5: Remove
(define (remove item lst) (
    cond
        ((null? lst) lst)
        ((= item (car lst)) (remove item (cdr lst)))
        (else (cons (car lst) (remove item (cdr lst))))
))

(expect (remove 3 nil) ())
(expect (remove 2 '(1 3 2)) (1 3))
(expect (remove 1 '(1 3 2)) (3 2))
(expect (remove 42 '(1 3 2)) (1 3 2))
(expect (remove 3 '(1 3 3 7)) (1 7))
