import sys
from app import app, db, Trees, Flowers, Vines, Cacti, Grasses, Aquatic

def seed_database():
    with app.app_context():
        print("Ensuring database tables exist...")
        db.create_all()

        print("Checking for new authentic Texas Flora data to insert...")
        
        # --- TREES (Top 30) ---
        trees = [
            Trees("Live Oak", "close_fullsize", "", "Quercus virginiana", "Tree", "", ""),
            Trees("Live Oak", "leaf", "", "Quercus virginiana", "Tree", "", ""),
            Trees("Live Oak", "bark", "", "Quercus virginiana", "Tree", "", ""),
            # ... (Keep all your other trees here) ...
            Trees("Anacua", "bark", "", "Ehretia anacua", "Tree", "", "")
        ]

        # THE BOUNCER: Only add the tree if it doesn't already exist!
        for tree in trees:
            exists = Trees.query.filter_by(name=tree.name, view_type=tree.view_type).first()
            if not exists:
                db.session.add(tree)

        # --- FLOWERS (Top 15) ---
        flowers = [
            Flowers("Texas Bluebonnet", "close_fullsize", "", "Lupinus texensis", "Flower", "", ""),
            # ... (Keep all your other flowers here) ...
            Flowers("Blue-eyed Grass", "close_fullsize", "", "Sisyrinchium campestre", "Flower", "", "")
        ]
        
        for flower in flowers:
            exists = Flowers.query.filter_by(name=flower.name).first()
            if not exists:
                db.session.add(flower)

        # --- VINES (Top 10) ---
        vines = [
            Vines("Mustang Grape", "close_fullsize", "", "Vitis mustangensis", "Vine", "", ""),
            # ... (Keep all your other vines here) ...
        ]
        for vine in vines:
            exists = Vines.query.filter_by(name=vine.name).first()
            if not exists:
                db.session.add(vine)

        # --- CACTI (Top 10) ---
        cacti = [
            Cacti("Texas Prickly Pear", "close_fullsize", "", "Opuntia engelmannii", "Cactus", "", ""),
            # ... (Keep all your other cacti here) ...
        ]
        for cactus in cacti:
            exists = Cacti.query.filter_by(name=cactus.name).first()
            if not exists:
                db.session.add(cactus)

        # --- GRASSES (Top 10) ---
        grasses = [
            Grasses("Buffalo Grass", "close_fullsize", "", "Bouteloua dactyloides", "Grass", "", ""),
            # ... (Keep all your other grasses here) ...
        ]
        for grass in grasses:
            exists = Grasses.query.filter_by(name=grass.name).first()
            if not exists:
                db.session.add(grass)

        # --- AQUATIC (Top 10) ---
        aquatic = [
            Aquatic("White Water Lily", "close_fullsize", "", "Nymphaea odorata", "Aquatic", "", ""),
            # ... (Keep all your other aquatic plants here) ...
        ]
        for aqua in aquatic:
            exists = Aquatic.query.filter_by(name=aqua.name).first()
            if not exists:
                db.session.add(aqua)

        # Commit all new additions to the database
        db.session.commit()
        print("Database sync complete! New data added safely.")

if __name__ == '__main__':
    seed_database()