(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (ascending? lst) (
    cond
        ((null? lst) #t)
        ((null? (cdr lst)) #t)
        ((<= (car lst) (cadr lst)) (ascending? (cdr lst)))
        (else #f)
))

(define (interleave lst1 lst2) (
    cond
        ((null? lst1) lst2)
        ((null? lst2) lst1)
        (else (
            cons (car lst1) (interleave lst2 (cdr lst1))
        ))
))

(define (my-filter func lst) (
    cond
        ((null? lst) lst)
        ((func (car lst)) (cons (car lst) (my-filter func (cdr lst))))
        (else (my-filter func (cdr lst)))
))

(define (no-repeats lst) (
    if (null? lst) lst (
        cons (car lst) (
            no-repeats (my-filter (lambda (x) (not (= x (car lst)))) (cdr lst))
        )
    )
))
