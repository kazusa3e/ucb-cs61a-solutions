(define (cadr lst) (car (cdr lst)))

(define (make-kwlist1 keys values) (
    list keys values
))

(define (get-keys-kwlist1 kwlist) (
    car kwlist
))

(define (get-values-kwlist1 kwlist) (
    cadr kwlist
))

(define (make-kwlist2 keys values) (
    if (null? keys)
        ()
        (cons (list (car keys) (car values)) (make-kwlist2 (cdr keys) (cdr values)))
))

(define (get-keys-kwlist2 kwlist) (
    if (null? kwlist)
        ()
        (cons (car (car kwlist)) (get-keys-kwlist2 (cdr kwlist)))
))

(define (get-values-kwlist2 kwlist) (
    if (null? kwlist)
        ()
        (cons
            (car (cdr (car kwlist))) (get-values-kwlist2 (cdr kwlist))
        )
))

(define (add-to-kwlist kwlist key value) (
    make-kwlist
        (append (get-keys-kwlist kwlist) (list key))
        (append (get-values-kwlist kwlist) (list value))
))

(define (get-first-from-kwlist kwlist key) (
    let (
        (keys (get-keys-kwlist kwlist))
        (values (get-values-kwlist kwlist))
    )
        (define (find-key keys values k) (
            cond
                ((null? keys) nil)
                ((equal? k (car keys)) (car values))
                (else (find-key (cdr keys) (cdr values) k))
        ))
        (find-key keys values key)
))

(define (prune-expr expr)
    (define (prune-helper lst flag) (
        cond
            ((null? lst) nil)
            ((= 0 flag) (
                cons (car lst) (prune-helper (cdr lst) 1)
            ))
            (else (
                prune-helper (cdr lst) 0
            ))
    ))
    (cons (car expr) (prune-helper (cdr expr) 0))
)

(define (curry-cook formals body) (
    if (= (length formals) 0)
        body
        (list 'lambda (list (car formals)) (curry-cook (cdr formals) body))
))

(define (curry-consume curries args) (
    if (= (length args) 0)
        curries
        (curry-consume (curries (car args)) (cdr args))
))
