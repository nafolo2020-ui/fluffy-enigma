def appliquer_remise(prix: float, pourcentage: float) -> float:
    """
    Calcule le prix après application d'une remise.

    Args:
        prix (float): Prix initial.
        pourcentage (float): Pourcentage de remise (entre 0 et 100).

    Returns:
        float: Prix final après remise, arrondi à 2 décimales.

    Raises:
        ValueError: Si le pourcentage est hors de l'intervalle [0, 100].
    """
    if not 0 <= pourcentage <= 100:
        raise ValueError("Pourcentage hors de l'intervalle 0-100")

    prix_final = prix * (1 - pourcentage / 100)

    return round(prix_final, 2)