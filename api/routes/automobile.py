from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from config import get_db
from sqlalchemy.orm import Session
from api.models.models import Automobile
from sqlalchemy import desc
from api.auth import oauth2

router = APIRouter()


@router.get("/automobile/5/premier_dernier(s)")
async def automobile(
    db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)
):
    """
        [1] : Afficher les cinq premières et dernières lignes.
    Args:
        db (Session, optional): _description_. Defaults to Depends(get_db).

    Returns:
        dict: un dictionnaire, concaténant les deux listes (les 5 premiers et derniers elements de la dataset)
    """
    # fixation du nombre d'élément
    nb_element = 5

    # Récuperation des données via sqlalchemy
    first_five = db.query(Automobile).all()[:nb_element]
    last_five = db.query(Automobile).all()[-nb_element:]
    return {
        f"Les {nb_element} premiers": first_five,
        f"Et les {nb_element} derniers": last_five,
    }


@router.get("/automobiles")
async def automobiles(
    db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)
):
    """
        [2] : Nettoyer et afficher l'ensemble de données.
    Remplacez toutes les valeurs de colonne qui contiennent ? n.a ou NaN par une valeur null
    Args:
        db (Session, optional): connection à la base de données. Defaults to Depends(get_db).

    Returns:
        dict: retourne la liste complète de tous les enregistrements de la dataset
    """
    return db.query(Automobile).all()


@router.get("/automobile/plus_cher_automobile")
async def automobile(
    db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)
):
    """
        [3] : Afficher le nom de l'entreprise automobile la plus chère.
    Args:
        db (Session, optional): base de données. Defaults to Depends(get_db).

    Returns:
        dict: Afficher le nom de l'entreprise automobile la plus chère.
    """
    auto = (
        db.query(Automobile.company, Automobile.price)
        .order_by(desc(Automobile.price))
        .first()
    )
    if auto is None:
        raise HTTPException(status_code=status.HTTP_404, detail="Erreur de la requête")

    return auto


@router.get("/automobiles/toyota")
async def automobile(
    db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)
):
    """
        [4] : Afficher tous les détails des voitures Toyota.

    Args:
        db (Session, optional): base de données. Defaults to Depends(get_db).

    Returns:
        dict: [4] : Afficher tous les détails des voitures Toyota.
    """
    autos = db.query(Automobile).filter(Automobile.company == "toyota").all()
    if autos is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"il n'y a pas de voiture avec la compagnie {Automobile.toyata}",
        )
    return autos


@router.get("/automobiles/infos")
async def automobile(
    db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)
):
    """
        [5] : Afficher et compter le nombre total de voitures par entreprise.

    Args:
        db (Session, optional): base de données. Defaults to Depends(get_db).

    Returns:
        dict:  Afficher et compter le nombre total de voitures par entreprise.
    """
    stmt = (
        "select company , count(company) as nb_cars from automobile a group by company"
    )
    res = db.execute(stmt)
    return res.fetchall()


@router.get("/automobiles/infos/avg_km/")
async def automobile(
    db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)
):
    """
        [6] : Afficher et trouver le kilométrage moyen de chaque constructeur automobile.

    Args:
        db (Session, optional): base de données. Defaults to Depends(get_db).

    Returns:
        dict:  Afficher et trouver le kilométrage moyen de chaque constructeur automobile.
    """
    stmt = "select company, avg(average_mileage) as avg_by_company from automobile a group by a.company"
    res = db.execute(stmt)

    return res.fetchall()


@router.get("/automobiles/infos/prices/")
async def automobile(
    db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)
):
    """
        [7] : Afficher et trier toutes les voitures par colonne Prix.

    Args:
        db (Session, optional): base de données. Defaults to Depends(get_db).

    Returns:
        dict: Afficher et trier toutes les voitures par colonne Prix.
    """
    return (
        db.query(Automobile.company, Automobile.price).order_by(Automobile.price).all()
    )


@router.get("/automobiles/infos/fusion")
async def automobile(
    db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)
):
    """
    [8] : Afficher et concaténer deux blocs de données en utilisant les conditions suivantes.
    Créez deux blocs de données à l'aide des deux dictionnaires suivants :
    GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
    japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]

    Args:
        db (Session, optional): base de données. Defaults to Depends(get_db).

    Returns:
        dict:Afficher et concaténer deux blocs de données en utilisant les conditions suivantes.
    """
    GermanCars = {
        "Company": ["Ford", "Mercedes", "BMV", "Audi"],
        "Price": [23845, 171995, 135925, 71400],
    }
    japaneseCars = {
        "Company": ["Toyota", "Honda", "Nissan", "Mitsubishi "],
        "Price": [29995, 23600, 61500, 58900],
    }
    tmp = {}
    for k in sorted(GermanCars):
        tmp[k] = [GermanCars[k] + japaneseCars[k]]

    return tmp
