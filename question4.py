def est_operateur(element: str) -> bool:
    """
    Vérifie si un élément est un opérateur arithmétique valide.
    
    Args:
        element: Chaîne de caractères à vérifier
        
    Returns:
        True si l'élément est un opérateur (+, -, *, /), False sinon
    """
    return element in ['+', '-', '*', '/']


def est_nombre(element: str) -> bool:
    """
    Vérifie si un élément peut être converti en nombre.
    
    Args:
        element: Chaîne de caractères à vérifier
        
    Returns:
        True si l'élément est un nombre valide, False sinon
    """
    try:
        float(element)
        return True
    except ValueError:
        return False


def appliquer_operation(operande_gauche: float, operande_droit: float,
                        operateur: str) -> float:
    """
    Applique une opération arithmétique entre deux opérandes.
    
    Args:
        operande_gauche: Premier opérande
        operande_droit: Second opérande
        operateur: Opérateur arithmétique (+, -, *, /)
        
    Returns:
        Résultat de l'opération
        
    Raises:
        ZeroDivisionError: Si division par zéro
        ValueError: Si opérateur invalide
    """
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else (_ for _ in ()).throw(
            ZeroDivisionError("Division par zéro impossible")
        )
    }
    
    if operateur not in operations:
        raise ValueError(f"Opérateur invalide : {operateur}")
    
    return operations[operateur](operande_gauche, operande_droit)


def valider_expression(elements: list[str]) -> None:
    """
    Valide la syntaxe d'une expression RPN.
    
    Args:
        elements: Liste des éléments de l'expression
        
    Raises:
        ValueError: Si l'expression est invalide
    """
    if not elements:
        raise ValueError("Expression vide")
    
    if est_operateur(elements[0]):
        raise ValueError("Opérateur en position initiale impossible")


def calculer_rpn(expression: str) -> float:
    """
    Calcule le résultat d'une expression en notation polonaise inverse.
    
    Args:
        expression: Expression RPN sous forme de chaîne
        
    Returns:
        Résultat du calcul
        
    Raises:
        ValueError: Si l'expression est invalide
        ZeroDivisionError: Si division par zéro
    """
    elements = expression.split()
    valider_expression(elements)
    
    pile = []
    
    for element in elements:
        if est_nombre(element):
            pile.append(float(element))
        elif est_operateur(element):
            if len(pile) < 2:
                raise ValueError(
                    f"Opérateur '{element}' nécessite deux opérandes"
                )
            
            operande_droit = pile.pop()
            operande_gauche = pile.pop()
            resultat = appliquer_operation(
                operande_gauche, operande_droit, element
            )
            pile.append(resultat)
        else:
            raise ValueError(f"Élément invalide : '{element}'")
    
    if len(pile) != 1:
        raise ValueError(
            "Expression incomplète : trop d'opérandes restants"
        )
    
    return pile[0]
