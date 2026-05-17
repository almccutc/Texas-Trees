import sys

# Import your Flask app instance, SQLAlchemy db, and models.
# NOTE: If your main file is named something other than 'app.py', 
# change 'from app import...' to 'from your_file_name import...'
from app import app, db, Trees, Flowers, Vines, Cacti, Grasses, Aquatic

def seed_database():
    with app.app_context():
        print("Recreating database tables...")
        # db.drop_all() # Uncomment this if you want to wipe the schema completely before rebuilding
        db.create_all()

        # Check if we already have data to prevent duplicate seeding
        if Trees.query.first():
            print("Database already contains data! Skipping seed.")
            return

        print("Inserting authentic Texas Flora data...")
        
        # --- TREES (Top 30) ---
        trees = [
            # Live Oak
            Trees("Live Oak", "close_fullsize", "", "Quercus virginiana", "Tree", "", ""),
            Trees("Live Oak", "leaf", "", "Quercus virginiana", "Tree", "", ""),
            Trees("Live Oak", "bark", "", "Quercus virginiana", "Tree", "", ""),
            
            # Pecan
            Trees("Pecan", "close_fullsize", "", "Carya illinoinensis", "Tree", "", ""),
            Trees("Pecan", "leaf", "", "Carya illinoinensis", "Tree", "", ""),
            Trees("Pecan", "bark", "", "Carya illinoinensis", "Tree", "", ""),

            # Texas Mountain Laurel
            Trees("Texas Mountain Laurel", "close_fullsize", "", "Dermatophyllum secundiflorum", "Tree", "", ""),
            Trees("Texas Mountain Laurel", "leaf", "", "Dermatophyllum secundiflorum", "Tree", "", ""),
            Trees("Texas Mountain Laurel", "bark", "", "Dermatophyllum secundiflorum", "Tree", "", ""),

            # Bald Cypress
            Trees("Bald Cypress", "close_fullsize", "", "Taxodium distichum", "Tree", "", ""),
            Trees("Bald Cypress", "leaf", "", "Taxodium distichum", "Tree", "", ""),
            Trees("Bald Cypress", "bark", "", "Taxodium distichum", "Tree", "", ""),

            # Honey Mesquite
            Trees("Honey Mesquite", "close_fullsize", "", "Prosopis glandulosa", "Tree", "", ""),
            Trees("Honey Mesquite", "leaf", "", "Prosopis glandulosa", "Tree", "", ""),
            Trees("Honey Mesquite", "bark", "", "Prosopis glandulosa", "Tree", "", ""),

            # Cedar Elm
            Trees("Cedar Elm", "close_fullsize", "", "Ulmus crassifolia", "Tree", "", ""),
            Trees("Cedar Elm", "leaf", "", "Ulmus crassifolia", "Tree", "", ""),
            Trees("Cedar Elm", "bark", "", "Ulmus crassifolia", "Tree", "", ""),

            # Southern Magnolia
            Trees("Southern Magnolia", "close_fullsize", "", "Magnolia grandiflora", "Tree", "", ""),
            Trees("Southern Magnolia", "leaf", "", "Magnolia grandiflora", "Tree", "", ""),
            Trees("Southern Magnolia", "bark", "", "Magnolia grandiflora", "Tree", "", ""),

            # Loblolly Pine
            Trees("Loblolly Pine", "close_fullsize", "", "Pinus taeda", "Tree", "", ""),
            Trees("Loblolly Pine", "leaf", "", "Pinus taeda", "Tree", "", ""),
            Trees("Loblolly Pine", "bark", "", "Pinus taeda", "Tree", "", ""),

            # Texas Redbud
            Trees("Texas Redbud", "close_fullsize", "", "Cercis canadensis var. texensis", "Tree", "", ""),
            Trees("Texas Redbud", "leaf", "", "Cercis canadensis var. texensis", "Tree", "", ""),
            Trees("Texas Redbud", "bark", "", "Cercis canadensis var. texensis", "Tree", "", ""),

            # Crape Myrtle
            Trees("Crape Myrtle", "close_fullsize", "", "Lagerstroemia indica", "Tree", "", ""),
            Trees("Crape Myrtle", "leaf", "", "Lagerstroemia indica", "Tree", "", ""),
            Trees("Crape Myrtle", "bark", "", "Lagerstroemia indica", "Tree", "", ""),

            # Ashe Juniper
            Trees("Ashe Juniper", "close_fullsize", "", "Juniperus ashei", "Tree", "", ""),
            Trees("Ashe Juniper", "leaf", "", "Juniperus ashei", "Tree", "", ""),
            Trees("Ashe Juniper", "bark", "", "Juniperus ashei", "Tree", "", ""),

            # Post Oak
            Trees("Post Oak", "close_fullsize", "", "Quercus stellata", "Tree", "", ""),
            Trees("Post Oak", "leaf", "", "Quercus stellata", "Tree", "", ""),
            Trees("Post Oak", "bark", "", "Quercus stellata", "Tree", "", ""),

            # Bur Oak
            Trees("Bur Oak", "close_fullsize", "", "Quercus macrocarpa", "Tree", "", ""),
            Trees("Bur Oak", "leaf", "", "Quercus macrocarpa", "Tree", "", ""),
            Trees("Bur Oak", "bark", "", "Quercus macrocarpa", "Tree", "", ""),

            # Shumard Oak
            Trees("Shumard Oak", "close_fullsize", "", "Quercus shumardii", "Tree", "", ""),
            Trees("Shumard Oak", "leaf", "", "Quercus shumardii", "Tree", "", ""),
            Trees("Shumard Oak", "bark", "", "Quercus shumardii", "Tree", "", ""),

            # Desert Willow
            Trees("Desert Willow", "close_fullsize", "", "Chilopsis linearis", "Tree", "", ""),
            Trees("Desert Willow", "leaf", "", "Chilopsis linearis", "Tree", "", ""),
            Trees("Desert Willow", "bark", "", "Chilopsis linearis", "Tree", "", ""),

            # Retama
            Trees("Retama", "close_fullsize", "", "Parkinsonia aculeata", "Tree", "", ""),
            Trees("Retama", "leaf", "", "Parkinsonia aculeata", "Tree", "", ""),
            Trees("Retama", "bark", "", "Parkinsonia aculeata", "Tree", "", ""),

            # Texas Ash
            Trees("Texas Ash", "close_fullsize", "", "Fraxinus texensis", "Tree", "", ""),
            Trees("Texas Ash", "leaf", "", "Fraxinus texensis", "Tree", "", ""),
            Trees("Texas Ash", "bark", "", "Fraxinus texensis", "Tree", "", ""),

            # Yaupon Holly
            Trees("Yaupon Holly", "close_fullsize", "", "Ilex vomitoria", "Tree", "", ""),
            Trees("Yaupon Holly", "leaf", "", "Ilex vomitoria", "Tree", "", ""),
            Trees("Yaupon Holly", "bark", "", "Ilex vomitoria", "Tree", "", ""),

            # Sweetgum
            Trees("Sweetgum", "close_fullsize", "", "Liquidambar styraciflua", "Tree", "", ""),
            Trees("Sweetgum", "leaf", "", "Liquidambar styraciflua", "Tree", "", ""),
            Trees("Sweetgum", "bark", "", "Liquidambar styraciflua", "Tree", "", ""),

            # Eastern Redcedar
            Trees("Eastern Redcedar", "close_fullsize", "", "Juniperus virginiana", "Tree", "", ""),
            Trees("Eastern Redcedar", "leaf", "", "Juniperus virginiana", "Tree", "", ""),
            Trees("Eastern Redcedar", "bark", "", "Juniperus virginiana", "Tree", "", ""),

            # Mexican Plum
            Trees("Mexican Plum", "close_fullsize", "", "Prunus mexicana", "Tree", "", ""),
            Trees("Mexican Plum", "leaf", "", "Prunus mexicana", "Tree", "", ""),
            Trees("Mexican Plum", "bark", "", "Prunus mexicana", "Tree", "", ""),

            # Hackberry
            Trees("Hackberry", "close_fullsize", "", "Celtis occidentalis", "Tree", "", ""),
            Trees("Hackberry", "leaf", "", "Celtis occidentalis", "Tree", "", ""),
            Trees("Hackberry", "bark", "", "Celtis occidentalis", "Tree", "", ""),

            # Sugarberry
            Trees("Sugarberry", "close_fullsize", "", "Celtis laevigata", "Tree", "", ""),
            Trees("Sugarberry", "leaf", "", "Celtis laevigata", "Tree", "", ""),
            Trees("Sugarberry", "bark", "", "Celtis laevigata", "Tree", "", ""),

            # Texas Persimmon
            Trees("Texas Persimmon", "close_fullsize", "", "Diospyros texana", "Tree", "", ""),
            Trees("Texas Persimmon", "leaf", "", "Diospyros texana", "Tree", "", ""),
            Trees("Texas Persimmon", "bark", "", "Diospyros texana", "Tree", "", ""),

            # American Sycamore
            Trees("American Sycamore", "close_fullsize", "", "Platanus occidentalis", "Tree", "", ""),
            Trees("American Sycamore", "leaf", "", "Platanus occidentalis", "Tree", "", ""),
            Trees("American Sycamore", "bark", "", "Platanus occidentalis", "Tree", "", ""),

            # Eastern Cottonwood
            Trees("Eastern Cottonwood", "close_fullsize", "", "Populus deltoides", "Tree", "", ""),
            Trees("Eastern Cottonwood", "leaf", "", "Populus deltoides", "Tree", "", ""),
            Trees("Eastern Cottonwood", "bark", "", "Populus deltoides", "Tree", "", ""),

            # Black Walnut
            Trees("Black Walnut", "close_fullsize", "", "Juglans nigra", "Tree", "", ""),
            Trees("Black Walnut", "leaf", "", "Juglans nigra", "Tree", "", ""),
            Trees("Black Walnut", "bark", "", "Juglans nigra", "Tree", "", ""),

            # Chinquapin Oak
            Trees("Chinquapin Oak", "close_fullsize", "", "Quercus muehlenbergii", "Tree", "", ""),
            Trees("Chinquapin Oak", "leaf", "", "Quercus muehlenbergii", "Tree", "", ""),
            Trees("Chinquapin Oak", "bark", "", "Quercus muehlenbergii", "Tree", "", ""),

            # Blackjack Oak
            Trees("Blackjack Oak", "close_fullsize", "", "Quercus marilandica", "Tree", "", ""),
            Trees("Blackjack Oak", "leaf", "", "Quercus marilandica", "Tree", "", ""),
            Trees("Blackjack Oak", "bark", "", "Quercus marilandica", "Tree", "", ""),

            # Anacua
            Trees("Anacua", "close_fullsize", "", "Ehretia anacua", "Tree", "", ""),
            Trees("Anacua", "leaf", "", "Ehretia anacua", "Tree", "", ""),
            Trees("Anacua", "bark", "", "Ehretia anacua", "Tree", "", "")
        ]

        db.session.add_all(trees)

        # --- FLOWERS (Top 15) ---
        flowers = [
            Flowers("Texas Bluebonnet", "close_fullsize", "", "Lupinus texensis", "Flower", "", ""),
            Flowers("Indian Blanket", "close_fullsize", "", "Gaillardia pulchella", "Flower", "", ""),
            Flowers("Pink Evening Primrose", "close_fullsize", "", "Oenothera speciosa", "Flower", "", ""),
            Flowers("Black-eyed Susan", "close_fullsize", "", "Rudbeckia hirta", "Flower", "", ""),
            Flowers("Mexican Hat", "close_fullsize", "", "Ratibida columnifera", "Flower", "", ""),
            Flowers("Texas Paintbrush", "close_fullsize", "", "Castilleja indivisa", "Flower", "", ""),
            Flowers("Plains Coreopsis", "close_fullsize", "", "Coreopsis tinctoria", "Flower", "", ""),
            Flowers("Drummond Phlox", "close_fullsize", "", "Phlox drummondii", "Flower", "", ""),
            Flowers("Texas Bluebell", "close_fullsize", "", "Eustoma exaltatum", "Flower", "", ""),
            Flowers("Purple Coneflower", "close_fullsize", "", "Echinacea purpurea", "Flower", "", ""),
            Flowers("Common Sunflower", "close_fullsize", "", "Helianthus annuus", "Flower", "", ""),
            Flowers("Winecup", "close_fullsize", "", "Callirhoe involuta", "Flower", "", ""),
            Flowers("Texas Lantana", "close_fullsize", "", "Lantana urticoides", "Flower", "", ""),
            Flowers("Standing Cypress", "close_fullsize", "", "Ipomopsis rubra", "Flower", "", ""),
            Flowers("Blue-eyed Grass", "close_fullsize", "", "Sisyrinchium campestre", "Flower", "", "")
        ]
        db.session.add_all(flowers)

        # --- VINES (Top 10) ---
        vines = [
            Vines("Mustang Grape", "close_fullsize", "", "Vitis mustangensis", "Vine", "", ""),
            Vines("Crossvine", "close_fullsize", "", "Bignonia capreolata", "Vine", "", ""),
            Vines("Virginia Creeper", "close_fullsize", "", "Parthenocissus quinquefolia", "Vine", "", ""),
            Vines("Coral Honeysuckle", "close_fullsize", "", "Lonicera sempervirens", "Vine", "", ""),
            Vines("Trumpet Vine", "close_fullsize", "", "Campsis radicans", "Vine", "", ""),
            Vines("Purple Passionflower", "close_fullsize", "", "Passiflora incarnata", "Vine", "", ""),
            Vines("Poison Ivy", "close_fullsize", "", "Toxicodendron radicans", "Vine", "", ""),
            Vines("Carolina Jessamine", "close_fullsize", "", "Gelsemium sempervirens", "Vine", "", ""),
            Vines("Southern Dewberry", "close_fullsize", "", "Rubus trivialis", "Vine", "", ""),
            Vines("Peppervine", "close_fullsize", "", "Nekemias arborea", "Vine", "", "")
        ]
        db.session.add_all(vines)

        # --- CACTI (Top 10) ---
        cacti = [
            Cacti("Texas Prickly Pear", "close_fullsize", "", "Opuntia engelmannii", "Cactus", "", ""),
            Cacti("Lace Cactus", "close_fullsize", "", "Echinocereus reichenbachii", "Cactus", "", ""),
            Cacti("Horse Crippler", "close_fullsize", "", "Echinocactus texensis", "Cactus", "", ""),
            Cacti("Claret Cup Cactus", "close_fullsize", "", "Echinocereus triglochidiatus", "Cactus", "", ""),
            Cacti("Nipple Cactus", "close_fullsize", "", "Mammillaria heyderi", "Cactus", "", ""),
            Cacti("Tasajillo", "close_fullsize", "", "Cylindropuntia leptocaulis", "Cactus", "", ""),
            Cacti("Blind Prickly Pear", "close_fullsize", "", "Opuntia rufida", "Cactus", "", ""),
            Cacti("Eagle Claws", "close_fullsize", "", "Echinocactus horizonthalonius", "Cactus", "", ""),
            Cacti("Strawberry Cactus", "close_fullsize", "", "Echinocereus stramineus", "Cactus", "", ""),
            Cacti("Texas Rainbow Cactus", "close_fullsize", "", "Echinocereus dasyacanthus", "Cactus", "", "")
        ]
        db.session.add_all(cacti)

        # --- GRASSES (Top 10) ---
        grasses = [
            Grasses("Buffalo Grass", "close_fullsize", "", "Bouteloua dactyloides", "Grass", "", ""),
            Grasses("Little Bluestem", "close_fullsize", "", "Schizachyrium scoparium", "Grass", "", ""),
            Grasses("Big Bluestem", "close_fullsize", "", "Andropogon gerardii", "Grass", "", ""),
            Grasses("Indiangrass", "close_fullsize", "", "Sorghastrum nutans", "Grass", "", ""),
            Grasses("Switchgrass", "close_fullsize", "", "Panicum virgatum", "Grass", "", ""),
            Grasses("Sideoats Grama", "close_fullsize", "", "Bouteloua curtipendula", "Grass", "", ""),
            Grasses("Blue Grama", "close_fullsize", "", "Bouteloua gracilis", "Grass", "", ""),
            Grasses("Texas Wintergrass", "close_fullsize", "", "Nassella leucotricha", "Grass", "", ""),
            Grasses("Inland Sea Oats", "close_fullsize", "", "Chasmanthium latifolium", "Grass", "", ""),
            Grasses("Gulf Muhly", "close_fullsize", "", "Muhlenbergia capillaris", "Grass", "", "")
        ]
        db.session.add_all(grasses)

        # --- AQUATIC (Top 10) ---
        aquatic = [
            Aquatic("White Water Lily", "close_fullsize", "", "Nymphaea odorata", "Aquatic", "", ""),
            Aquatic("American Lotus", "close_fullsize", "", "Nelumbo lutea", "Aquatic", "", ""),
            Aquatic("Pickerelweed", "close_fullsize", "", "Pontederia cordata", "Aquatic", "", ""),
            Aquatic("Common Duckweed", "close_fullsize", "", "Lemna minor", "Aquatic", "", ""),
            Aquatic("Coontail", "close_fullsize", "", "Ceratophyllum demersum", "Aquatic", "", ""),
            Aquatic("Water Hyacinth", "close_fullsize", "", "Eichhornia crassipes", "Aquatic", "", ""),
            Aquatic("Broadleaf Arrowhead", "close_fullsize", "", "Sagittaria latifolia", "Aquatic", "", ""),
            Aquatic("Spatterdock", "close_fullsize", "", "Nuphar advena", "Aquatic", "", ""),
            Aquatic("Water Pennywort", "close_fullsize", "", "Hydrocotyle umbellata", "Aquatic", "", ""),
            Aquatic("Southern Naiad", "close_fullsize", "", "Najas guadalupensis", "Aquatic", "", "")
        ]
        db.session.add_all(aquatic)

        # Commit all changes to the database
        db.session.commit()
        print("Database successfully seeded! You can now run your Flask app.")

if __name__ == '__main__':
    seed_database()