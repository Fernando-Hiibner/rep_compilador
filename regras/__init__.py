REGRAS = {
    "E" : {
        "id" : "E->TS",
        "num" : "E->TS",
        "(" : "E->TS"
    },
    "T" : {
        "id" : "T->FG",
        "num": "T->FG"
    },
    "S" : {
        "+" : "S->+TS",
        "-" : "S->-TS",
        ")" : "S-> (lambda)",
        "&" : "S-> (lambda)"
    },
    "G" : {
        "+" : "(lambda)",
        "-" : "(lambda)",
        "*" : "*FG",
        "/" : "/FG",
        ")" : "(lambda)",
        "$" : "(lambda)"
    },
    "F" : {
        "id": "F->id",
        "num" : "F->num",
        "(" : "(E)"
    }
}