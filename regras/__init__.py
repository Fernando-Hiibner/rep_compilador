REGRAS = {
    "E" : {
        "id" : ["T", "S"],
        "num" : ["T", "S"],
        "(" : ["T", "S"]
    },
    "T" : {
        "id" : ["F", "G"],
        "num": ["F", "G"],
        "(" : ["F", "G"]
    },
    "S" : {
        "+" : ["+", "T", "S"],
        "-" : ["-", "T", "S"],
        ")" : ["§"],
        "$" : ["§"]
    },
    "G" : {
        "+" : ["§"],
        "-" : ["§"],
        "*" : ["*", "F", "G"],
        "/" : ["/", "F", "G"],
        ")" : ["§"],
        "$" : ["§"]
    },
    "F" : {
        "id": ["id"],
        "num" : ["num"],
        "(" : ["(", "E", ")"]
    }
}

"""
(id + num)
( - id - + - num - )

REGRAS["F"]["("] -> (
REGRAS["F"]["("] -> E["("] -> TS
REGRAS["F"]["("] -> E["("] -> TS -> T["id"] -> FG
REGRAS["F"]["("] -> E["("] -> TS -> T["id"] -> FG -> F["id"] -> True
REGRAS["F"]["("] -> E["("] -> TS -> T["id"] -> FG -> G["+"]  -> lambda(+)
REGRAS["F"]["("] -> E["("] -> TS -> T["id"] -> FG -> lambda(+)
REGRAS["F"]["("] -> E["("] -> TS -> T["id"] -> lambda(+)
REGRAS["F"]["("] -> E["("] -> TS -> S["lambda(+)"] -> +TS
REGRAS["F"]["("] -> E["("] -> TS -> S["lambda(+)"] -> +TS["+"] -> True(+)
REGRAS["F"]["("] -> E["("] -> TS -> S["lambda(+)"] -> +TS["num"] -> T["num"] -> FG
REGRAS["F"]["("] -> E["("] -> TS -> S["lambda(+)"] -> +TS["num"] -> T["num"] -> FG -> F["num"] -> True
REGRAS["F"]["("] -> E["("] -> TS -> S["lambda(+)"] -> +TS["num"] -> T["num"] -> FG -> True
REGRAS["F"]["("] -> E["("] -> TS -> S["lambda(+)"] -> +TS["num"] -> T["num"] -> FG -> G[")"] -> lambda(")")
REGRAS["F"]["("] -> E["("] -> TS -> S["lambda(+)"] -> +TS["num"] -> S[lambda(")")] -> lambda(")")
REGRAS["F"]["("] -> E["("] -> TS -> lambda(")")
REGRAS["F"]["("] -> E["("] -> lambda(")") -> True
REGRAS["F"]["("] -> True
"""