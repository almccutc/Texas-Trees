import sys

# Import your Flask app instance, SQLAlchemy db, and models from app.py
from app import app, db, Trees, Flowers, Vines, Cacti, Grasses, Aquatic

def seed_database():
    with app.app_context():
        print("Ensuring database tables exist...")
        db.create_all()

        print("Checking for new authentic Texas Flora data to insert...")
        
        # --- TREES (60 Unique Species - 180 total image records) ---
        trees = [
            # 1. Live Oak
            Trees("Live Oak", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/live_oak_335892366-min.jpeg", "Quercus virginiana", "Tree", "", ""),
            Trees("Live Oak", "leaf", "", "Quercus virginiana", "Tree", "", ""),
            Trees("Live Oak", "bark", "", "Quercus virginiana", "Tree", "", ""),

            # 2. Box Elder
            Trees("Box Elder", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/box_elder_full_1.jpeg", "Acer negundo", "Tree", "", ""),
            Trees("Box Elder", "leaf", "", "Acer negundo", "Tree", "", ""),
            Trees("Box Elder", "bark", "", "Acer negundo", "Tree", "", ""),
            
            # 3. Pecan
            Trees("Pecan", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/pecan_17094154-min.jpeg", "Carya illinoinensis", "Tree", "", ""),
            Trees("Pecan", "leaf", "", "Carya illinoinensis", "Tree", "", ""),
            Trees("Pecan", "bark", "", "Carya illinoinensis", "Tree", "", ""),

            # 4. Texas Mountain Laurel
            Trees("Texas Mountain Laurel", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/texas_mountain_laurel_266042203-min.jpeg", "Dermatophyllum secundiflorum", "Tree", "", ""),
            Trees("Texas Mountain Laurel", "leaf", "", "Dermatophyllum secundiflorum", "Tree", "", ""),
            Trees("Texas Mountain Laurel", "bark", "", "Dermatophyllum secundiflorum", "Tree", "", ""),

            # 5. Bald Cypress
            Trees("Bald Cypress", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/bald_cypress_fullsize_1.jpeg", "Taxodium distichum", "Tree", "", ""),
            Trees("Bald Cypress", "leaf", "", "Taxodium distichum", "Tree", "", ""),
            Trees("Bald Cypress", "bark", "", "Taxodium distichum", "Tree", "", ""),

            # 6. Honey Mesquite
            Trees("Honey Mesquite", "close_fullsize", "", "Prosopis glandulosa", "Tree", "", ""),
            Trees("Honey Mesquite", "leaf", "", "Prosopis glandulosa", "Tree", "", ""),
            Trees("Honey Mesquite", "bark", "", "Prosopis glandulosa", "Tree", "", ""),

            # 7. Cedar Elm
            Trees("Cedar Elm", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/cedar_elm_71342713-min.jpeg", "Ulmus crassifolia", "Tree", "", ""),
            Trees("Cedar Elm", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/cedar_elm_leaf1.jpeg", "Ulmus crassifolia", "Tree", "", ""),
            Trees("Cedar Elm", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/cedar_elm_bark.jpeg", "Ulmus crassifolia", "Tree", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/cedar_elm_bark.jpeg", ""),

            # 8. Southern Magnolia
            Trees("Southern Magnolia", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/southern_magnolia_246625979-min.jpeg", "Magnolia grandiflora", "Tree", "", ""),
            Trees("Southern Magnolia", "leaf", "", "Magnolia grandiflora", "Tree", "", ""),
            Trees("Southern Magnolia", "bark", "", "Magnolia grandiflora", "Tree", "", ""),

            # 9. Loblolly Pine
            Trees("Loblolly Pine", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/loblolly_pine_168861849-min.jpeg", "Pinus taeda", "Tree", "", ""),
            Trees("Loblolly Pine", "leaf", "", "Pinus taeda", "Tree", "", ""),
            Trees("Loblolly Pine", "bark", "", "Pinus taeda", "Tree", "", ""),

            # 10. Texas Redbud
            Trees("Texas Redbud", "close_fullsize", "", "Cercis canadensis var. texensis", "Tree", "", ""),
            Trees("Texas Redbud", "leaf", "", "Cercis canadensis var. texensis", "Tree", "", ""),
            Trees("Texas Redbud", "bark", "", "Cercis canadensis var. texensis", "Tree", "", ""),

            # 11. Crape Myrtle
            Trees("Crape Myrtle", "close_fullsize", "", "Lagerstroemia indica", "Tree", "", ""),
            Trees("Crape Myrtle", "leaf", "", "Lagerstroemia indica", "Tree", "", ""),
            Trees("Crape Myrtle", "bark", "", "Lagerstroemia indica", "Tree", "", ""),

            # 12. Ashe Juniper
            Trees("Ashe Juniper", "close_fullsize", "", "Juniperus ashei", "Tree", "", ""),
            Trees("Ashe Juniper", "leaf", "", "Juniperus ashei", "Tree", "", ""),
            Trees("Ashe Juniper", "bark", "", "Juniperus ashei", "Tree", "", ""),

            # 13. Post Oak
            Trees("Post Oak", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/post_oak_69964216-min.jpeg", "Quercus stellata", "Tree", "", ""),
            Trees("Post Oak", "leaf", "", "Quercus stellata", "Tree", "", ""),
            Trees("Post Oak", "bark", "", "Quercus stellata", "Tree", "", ""),

            # 14. Bur Oak
            Trees("Bur Oak", "close_fullsize", "", "Quercus macrocarpa", "Tree", "", ""),
            Trees("Bur Oak", "leaf", "", "Quercus macrocarpa", "Tree", "", ""),
            Trees("Bur Oak", "bark", "", "Quercus macrocarpa", "Tree", "", ""),

            # 15. Shumard Oak
            Trees("Shumard Oak", "close_fullsize", "", "Quercus shumardii", "Tree", "", ""),
            Trees("Shumard Oak", "leaf", "", "Quercus shumardii", "Tree", "", ""),
            Trees("Shumard Oak", "bark", "", "Quercus shumardii", "Tree", "", ""),

            # 16. Desert Willow
            Trees("Desert Willow", "close_fullsize", "", "Chilopsis linearis", "Tree", "", ""),
            Trees("Desert Willow", "leaf", "", "Chilopsis linearis", "Tree", "", ""),
            Trees("Desert Willow", "bark", "", "Chilopsis linearis", "Tree", "", ""),

            # 17. Retama
            Trees("Retama", "close_fullsize", "", "Parkinsonia aculeata", "Tree", "", ""),
            Trees("Retama", "leaf", "", "Parkinsonia aculeata", "Tree", "", ""),
            Trees("Retama", "bark", "", "Parkinsonia aculeata", "Tree", "", ""),

            # 18. Texas Ash
            Trees("Texas Ash", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/texas_ash_947070-min.jpeg", "Fraxinus texensis", "Tree", "", ""),
            Trees("Texas Ash", "leaf", "", "Fraxinus texensis", "Tree", "", ""),
            Trees("Texas Ash", "bark", "", "Fraxinus texensis", "Tree", "", ""),

            # 19. Yaupon Holly
            Trees("Yaupon Holly", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/yaupon_holly_5907614-min.jpeg", "Ilex vomitoria", "Tree", "", ""),
            Trees("Yaupon Holly", "leaf", "", "Ilex vomitoria", "Tree", "", ""),
            Trees("Yaupon Holly", "bark", "", "Ilex vomitoria", "Tree", "", ""),

            # 20. Sweetgum
            Trees("Sweetgum", "close_fullsize", "", "Liquidambar styraciflua", "Tree", "", ""),
            Trees("Sweetgum", "leaf", "", "Liquidambar styraciflua", "Tree", "", ""),
            Trees("Sweetgum", "bark", "", "Liquidambar styraciflua", "Tree", "", ""),

            # 21. Eastern Redcedar
            Trees("Eastern Redcedar", "close_fullsize", "", "Juniperus virginiana", "Tree", "", ""),
            Trees("Eastern Redcedar", "leaf", "", "Juniperus virginiana", "Tree", "", ""),
            Trees("Eastern Redcedar", "bark", "", "Juniperus virginiana", "Tree", "", ""),

            # 22. Mexican Plum
            Trees("Mexican Plum", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/mexican_plum_44227239-min.jpeg", "Prunus mexicana", "Tree", "", ""),
            Trees("Mexican Plum", "leaf", "", "Prunus mexicana", "Tree", "", ""),
            Trees("Mexican Plum", "bark", "", "Prunus mexicana", "Tree", "", ""),

            # 23. Hackberry
            Trees("Hackberry", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/hackberry_324208578-min.jpeg", "Celtis occidentalis", "Tree", "", ""),
            Trees("Hackberry", "leaf", "", "Celtis occidentalis", "Tree", "", ""),
            Trees("Hackberry", "bark", "", "Celtis occidentalis", "Tree", "", ""),

            # 24. Sugarberry
            Trees("Sugarberry", "close_fullsize", "", "Celtis laevigata", "Tree", "", ""),
            Trees("Sugarberry", "leaf", "", "Celtis laevigata", "Tree", "", ""),
            Trees("Sugarberry", "bark", "", "Celtis laevigata", "Tree", "", ""),

            # 25. Texas Persimmon
            Trees("Texas Persimmon", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/Texas_persimmon_full_1.jpeg", "Diospyros texana", "Tree", "", ""),
            Trees("Texas Persimmon", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/Texas_persimmon_leaf_1.jpeg", "Diospyros texana", "Tree", "", ""),
            Trees("Texas Persimmon", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/Texas_persimmon_bark_1.jpeg", "Diospyros texana", "Tree", "", ""),

            # 26. American Sycamore
            Trees("American Sycamore", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/american_sycamore_84788584-min.jpeg", "Platanus occidentalis", "Tree", "", ""),
            Trees("American Sycamore", "leaf", "", "Platanus occidentalis", "Tree", "", ""),
            Trees("American Sycamore", "bark", "", "Platanus occidentalis", "Tree", "", ""),

            # 27. Eastern Cottonwood
            Trees("Eastern Cottonwood", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/cottonwood_68252199-min.jpeg", "Populus deltoides", "Tree", "", ""),
            Trees("Eastern Cottonwood", "leaf", "", "Populus deltoides", "Tree", "", ""),
            Trees("Eastern Cottonwood", "bark", "", "Populus deltoides", "Tree", "", ""),

            # 28. Black Walnut
            Trees("Black Walnut", "close_fullsize", "", "Juglans nigra", "Tree", "", ""),
            Trees("Black Walnut", "leaf", "", "Juglans nigra", "Tree", "", ""),
            Trees("Black Walnut", "bark", "", "Juglans nigra", "Tree", "", ""),

            # 29. Chinquapin Oak
            Trees("Chinquapin Oak", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/chinkapin_oak_165800321-min.jpeg", "Quercus muehlenbergii", "Tree", "", ""),
            Trees("Chinquapin Oak", "leaf", "", "Quercus muehlenbergii", "Tree", "", ""),
            Trees("Chinquapin Oak", "bark", "", "Quercus muehlenbergii", "Tree", "", ""),

            # 30. Blackjack Oak
            Trees("Blackjack Oak", "close_fullsize", "", "Quercus marilandica", "Tree", "", ""),
            Trees("Blackjack Oak", "leaf", "", "Quercus marilandica", "Tree", "", ""),
            Trees("Blackjack Oak", "bark", "", "Quercus marilandica", "Tree", "", ""),

            # 31. Anacua
            Trees("Anacua", "close_fullsize", "", "Ehretia anacua", "Tree", "", ""),
            Trees("Anacua", "leaf", "", "Ehretia anacua", "Tree", "", ""),
            Trees("Anacua", "bark", "", "Ehretia anacua", "Tree", "", ""),

            # 32. Texas Pistache
            Trees("Texas Pistache", "close_fullsize", "", "Pistacia texana", "Tree", "", ""),
            Trees("Texas Pistache", "leaf", "", "Pistacia texana", "Tree", "", ""),
            Trees("Texas Pistache", "bark", "", "Pistacia texana", "Tree", "", ""),

            # 33. Texas Ebony
            Trees("Texas Ebony", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/texas_ebony_2279225-min.jpeg", "Ebenopsis ebano", "Tree", "", ""),
            Trees("Texas Ebony", "leaf", "", "Ebenopsis ebano", "Tree", "", ""),
            Trees("Texas Ebony", "bark", "", "Ebenopsis ebano", "Tree", "", ""),

            # 34. Huisache
            Trees("Huisache", "close_fullsize", "", "Vachellia farnesiana", "Tree", "", ""),
            Trees("Huisache", "leaf", "", "Vachellia farnesiana", "Tree", "", ""),
            Trees("Huisache", "bark", "", "Vachellia farnesiana", "Tree", "", ""),

            # 35. Guajillo
            Trees("Guajillo", "close_fullsize", "", "Senegalia berlandieri", "Tree", "", ""),
            Trees("Guajillo", "leaf", "", "Senegalia berlandieri", "Tree", "", ""),
            Trees("Guajillo", "bark", "", "Senegalia berlandieri", "Tree", "", ""),

            # 36. Goldenball Leadtree
            Trees("Goldenball Leadtree", "close_fullsize", "", "Leucaena retusa", "Tree", "", ""),
            Trees("Goldenball Leadtree", "leaf", "", "Leucaena retusa", "Tree", "", ""),
            Trees("Goldenball Leadtree", "bark", "", "Leucaena retusa", "Tree", "", ""),

            # 37. Texas Madrone
            Trees("Texas Madrone", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/texas_madrone_347099237-min.jpeg", "Arbutus xalapensis", "Tree", "", ""),
            Trees("Texas Madrone", "leaf", "", "Arbutus xalapensis", "Tree", "", ""),
            Trees("Texas Madrone", "bark", "", "Arbutus xalapensis", "Tree", "", ""),

            # 38. Chisos Red Oak
            Trees("Chisos Red Oak", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/texas_red_oak_85298162-min.jpeg", "Quercus gravesii", "Tree", "", ""),
            Trees("Chisos Red Oak", "leaf", "", "Quercus gravesii", "Tree", "", ""),
            Trees("Chisos Red Oak", "bark", "", "Quercus gravesii", "Tree", "", ""),

            # 39. Bigtooth Maple
            Trees("Bigtooth Maple", "close_fullsize", "", "Acer grandidentatum", "Tree", "", ""),
            Trees("Bigtooth Maple", "leaf", "", "Acer grandidentatum", "Tree", "", ""),
            Trees("Bigtooth Maple", "bark", "", "Acer grandidentatum", "Tree", "", ""),

            # 40. Red Maple
            Trees("Red Maple", "close_fullsize", "", "Acer rubrum", "Tree", "", ""),
            Trees("Red Maple", "leaf", "", "Acer rubrum", "Tree", "", ""),
            Trees("Red Maple", "bark", "", "Acer rubrum", "Tree", "", ""),

            # 41. Mexican Buckeye
            Trees("Mexican Buckeye", "close_fullsize", "", "Ungnadia speciosa", "Tree", "", ""),
            Trees("Mexican Buckeye", "leaf", "", "Ungnadia speciosa", "Tree", "", ""),
            Trees("Mexican Buckeye", "bark", "", "Ungnadia speciosa", "Tree", "", ""),

            # 42. Carolina Basswood
            Trees("Carolina Basswood", "close_fullsize", "", "Tilia americana var. caroliniana", "Tree", "", ""),
            Trees("Carolina Basswood", "leaf", "", "Tilia americana var. caroliniana", "Tree", "", ""),
            Trees("Carolina Basswood", "bark", "", "Tilia americana var. caroliniana", "Tree", "", ""),

            # 43. Rusty Blackhaw
            Trees("Rusty Blackhaw", "close_fullsize", "", "Viburnum rufidulum", "Tree", "", ""),
            Trees("Rusty Blackhaw", "leaf", "", "Viburnum rufidulum", "Tree", "", ""),
            Trees("Rusty Blackhaw", "bark", "", "Viburnum rufidulum", "Tree", "", ""),

            # 44. Two-wing Silverbell
            Trees("Two-wing Silverbell", "close_fullsize", "", "Halesia diptera", "Tree", "", ""),
            Trees("Two-wing Silverbell", "leaf", "", "Halesia diptera", "Tree", "", ""),
            Trees("Two-wing Silverbell", "bark", "", "Halesia diptera", "Tree", "", ""),

            # 45. Flowering Dogwood
            Trees("Flowering Dogwood", "close_fullsize", "", "Cornus florida", "Tree", "", ""),
            Trees("Flowering Dogwood", "leaf", "", "Cornus florida", "Tree", "", ""),
            Trees("Flowering Dogwood", "bark", "", "Cornus florida", "Tree", "", ""),

            # 46. Longleaf Pine
            Trees("Longleaf Pine", "close_fullsize", "", "Pinus palustris", "Tree", "", ""),
            Trees("Longleaf Pine", "leaf", "", "Pinus palustris", "Tree", "", ""),
            Trees("Longleaf Pine", "bark", "", "Pinus palustris", "Tree", "", ""),

            # 47. Shortleaf Pine
            Trees("Shortleaf Pine", "close_fullsize", "", "Pinus echinata", "Tree", "", ""),
            Trees("Shortleaf Pine", "leaf", "", "Pinus echinata", "Tree", "", ""),
            Trees("Shortleaf Pine", "bark", "", "Pinus echinata", "Tree", "", ""),

            # 48. Overcup Oak
            Trees("Overcup Oak", "close_fullsize", "", "Quercus lyrata", "Tree", "", ""),
            Trees("Overcup Oak", "leaf", "", "Quercus lyrata", "Tree", "", ""),
            Trees("Overcup Oak", "bark", "", "Quercus lyrata", "Tree", "", ""),

            # 49. Water Oak
            Trees("Water Oak", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/water_oak_11503888-min.jpeg", "Quercus nigra", "Tree", "", ""),
            Trees("Water Oak", "leaf", "", "Quercus nigra", "Tree", "", ""),
            Trees("Water Oak", "bark", "", "Quercus nigra", "Tree", "", ""),

            # 50. Willow Oak
            Trees("Willow Oak", "close_fullsize", "", "Quercus phellos", "Tree", "", ""),
            Trees("Willow Oak", "leaf", "", "Quercus phellos", "Tree", "", ""),
            Trees("Willow Oak", "bark", "", "Quercus phellos", "Tree", "", ""),

            # 51. American Elm
            Trees("American Elm", "close_fullsize", "", "Ulmus americana", "Tree", "", ""),
            Trees("American Elm", "leaf", "", "Ulmus americana", "Tree", "", ""),
            Trees("American Elm", "bark", "", "Ulmus americana", "Tree", "", ""),

            # 52. Winged Elm
            Trees("Winged Elm", "close_fullsize", "", "Ulmus alata", "Tree", "", ""),
            Trees("Winged Elm", "leaf", "", "Ulmus alata", "Tree", "", ""),
            Trees("Winged Elm", "bark", "", "Ulmus alata", "Tree", "", ""),

            # 53. Black Cherry
            Trees("Black Cherry", "close_fullsize", "", "Prunus serotina", "Tree", "", ""),
            Trees("Black Cherry", "leaf", "", "Prunus serotina", "Tree", "", ""),
            Trees("Black Cherry", "bark", "", "Prunus serotina", "Tree", "", ""),

            # 54. Carolina Buckthorn
            Trees("Carolina Buckthorn", "close_fullsize", "", "Frangula caroliniana", "Tree", "", ""),
            Trees("Carolina Buckthorn", "leaf", "", "Frangula caroliniana", "Tree", "", ""),
            Trees("Carolina Buckthorn", "bark", "", "Frangula caroliniana", "Tree", "", ""),

            # 55. Common Buttonbush
            Trees("Common Buttonbush", "close_fullsize", "", "Cephalanthus occidentalis", "Tree", "", ""),
            Trees("Common Buttonbush", "leaf", "", "Cephalanthus occidentalis", "Tree", "", ""),
            Trees("Common Buttonbush", "bark", "", "Cephalanthus occidentalis", "Tree", "", ""),

            # 56. Green Ash
            Trees("Green Ash", "close_fullsize", "", "Fraxinus pennsylvanica", "Tree", "", ""),
            Trees("Green Ash", "leaf", "", "Fraxinus pennsylvanica", "Tree", "", ""),
            Trees("Green Ash", "bark", "", "Fraxinus pennsylvanica", "Tree", "", ""),

            # 57. White Ash
            Trees("White Ash", "close_fullsize", "", "Fraxinus americana", "Tree", "", ""),
            Trees("White Ash", "leaf", "", "Fraxinus americana", "Tree", "", ""),
            Trees("White Ash", "bark", "", "Fraxinus americana", "Tree", "", ""),

            # 58. Texas Mulberry
            Trees("Texas Mulberry", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/red_mulberry_224125363-min.jpeg", "Morus microphylla", "Tree", "", ""),
            Trees("Texas Mulberry", "leaf", "", "Morus microphylla", "Tree", "", ""),
            Trees("Texas Mulberry", "bark", "", "Morus microphylla", "Tree", "", ""),

            # 59. Red Mulberry
            Trees("Red Mulberry", "close_fullsize", "", "Morus rubra", "Tree", "", ""),
            Trees("Red Mulberry", "leaf", "", "Morus rubra", "Tree", "", ""),
            Trees("Red Mulberry", "bark", "", "Morus rubra", "Tree", "", ""),

            # 60. Sassafras
            Trees("Sassafras", "close_fullsize", "", "Sassafras albidum", "Tree", "", ""),
            Trees("Sassafras", "leaf", "", "Sassafras albidum", "Tree", "", ""),
            Trees("Sassafras", "bark", "", "Sassafras albidum", "Tree", "", "")
        ]

        # bouncer loop for trees -- checking both plant_name AND image_type (leaf/bark/close)
        # Updated bouncer loop for trees -- now updates URLs if they changed!
        for tree in trees:
            exists = Trees.query.filter_by(plant_name=tree.plant_name, image_type=tree.image_type).first()
            if not exists:
                db.session.add(tree)
            else:
                # If the tree exists, update its image_url with your new URL
                if exists.image_url != tree.image_url:
                    exists.image_url = tree.image_url
                    print(f"Updated URL for {tree.plant_name} ({tree.image_type})")
                    
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
        
        for flower in flowers:
            exists = Flowers.query.filter_by(plant_name=flower.plant_name).first()
            if not exists:
                db.session.add(flower)

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
        
        for vine in vines:
            exists = Vines.query.filter_by(plant_name=vine.plant_name).first()
            if not exists:
                db.session.add(vine)

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
        
        for cactus in cacti:
            exists = Cacti.query.filter_by(plant_name=cactus.plant_name).first()
            if not exists:
                db.session.add(cactus)

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
        
        for grass in grasses:
            exists = Grasses.query.filter_by(plant_name=grass.plant_name).first()
            if not exists:
                db.session.add(grass)

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
        
        for aqua in aquatic:
            exists = Aquatic.query.filter_by(plant_name=aqua.plant_name).first()
            if not exists:
                db.session.add(aqua)

        # Commit all changes to the database
        db.session.commit()
        print("Database sync complete! New flora data added safely.")

if __name__ == '__main__':
    seed_database()