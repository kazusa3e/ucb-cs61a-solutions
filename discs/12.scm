;; Q1: WWSD? Quasiquotation
;; scm> '(1 x 3)
;; (1 x 3)
;; scm> (define x 2)
;; x
;; scm> `(1 x 3)
;; (1 x 3)
;; scm> `(1 ,x 3)
;; (1 2 3)
;; scm> '(1 ,x 3)
;; (1 (unquote x) 3)
;; scm> `(,1 x 3)
;; (1 x 3)
;; scm> `,(+ 1 x 3)
;; 6
;; scm> `(1 (,x) 3)
;; (1 (2) 3)
;; scm> `(1 ,(+ x 2) 3)
;; (1 4 3)
;; scm> (define y 3)
;; y
;; scm> `(x ,(* y x) y)
;; (x 6 y)
;; scm> `(1 ,(cons x (list y 4)) 5)
;; (1 (2 3 4) 5)

;; Q2: WWSD? Eval and Apply
;; scm> (define add-numbers '(+ 1 2))
;; add-numbers
;; scm> add-numbers
;; (+ 1 2)
;; scm> (eval add-numbers)
;; 3
;; scm> (apply + '(1 2))
;; 3
;; scm> (define expr '(lambda (a b) (+ a b)))
;; expr
;; scm> expr
;; (lambda (a b) (+ a b))
;; scm> (define adder-func (eval expr))
;; adder-func
;; scm> (apply adder-func '(1 2))
;; 3
;; scm> (define make-list (cons 'list '(1 2 3)))
;; make-list
;; scm> make-list
;; (list 1 2 3)
;; scm> (apply list '(1 2 3))
;; (1 2 3)

;; Q3: Geometric Sequence
(define (geom n f) (
    if (= n 0)
        1
        `(* ,(geom (- n 1) f) ,f)
))

(define expr (geom 1 5))
(expect expr (* 1 5))
(expect (eval expr) 5)

(define expr2 (geom 2 5))
(expect expr2 (* (* 1 5) 5))
(expect (eval expr2) 25)

;; Q4: Make Or
(define (make-or expr1 expr2)
    `(let ((v1 ,expr1))
            (if v1 v1 ,expr2))
)

;; Q5: Make "Make Or"
(define (make-make-or)
    `(define (make-or expr1 expr2)
        `(let ((v1 ,expr1))
            (if v1 v1 ,expr2))
    )
)

scm> (make-make-or)
(define (make-or expr1 expr2) (quasiquote (let ((v1 (unquote expr1))) (if v1 v1 (unquote expr2)))))
scm> (eval (make-make-or))
make-or
scm> (eval (eval (make-make-or)))
(lambda (expr1 expr2) (quasiquote (let ((v1 (unquote expr1))) (if v1 v1 (unquote expr2)))))
scm> (apply (eval (eval (make-make-or))) '(#t (/ 1 0)))
(let ((v1 #t)) (if v1 v1 (/ 1 0)))
scm> (eval (apply (eval (eval (make-make-or))) '(#t (/ 1 0))))
#t
