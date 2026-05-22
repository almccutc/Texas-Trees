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
            Trees("Live Oak", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/live_oak.jpeg", "Quercus virginiana", "Tree", "iNaturalist Photo 40943585, (c) Rich Sommer", ""),
            Trees("Live Oak", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/liveoakbark.jpg", "Quercus virginiana", "Tree", "iNaturalist Photo 40943585, (c) CK2AZ", ""),

            # 2. Box Elder
            Trees("Box Elder", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/box_elder_full_1.jpeg", "Acer negundo", "Tree", "", ""),
            Trees("Box Elder", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/boxelderleaf.jpeg", "Acer negundo", "Tree", "iNaturalist Photo 3748489, (c) Sam Kieschnick", ""),
            Trees("Box Elder", "bark", "", "Acer negundo", "Tree", "iNaturalist Photo 479095624, (c) ashleyrsteel", ""),
            
            # 3. Pecan
            Trees("Pecan", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/pecan_17094154-min.jpeg", "Carya illinoinensis", "Tree", "", ""),
            Trees("Pecan", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/pecanleaf.jpeg", "Carya illinoinensis", "Tree", "Photo 374616741, (c) Michelle W. ", ""),
            Trees("Pecan", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/pecanbark.jpeg", "Carya illinoinensis", "Tree", "Photo 374616876, (c) Michelle W.", ""),

            # 4. Texas Mountain Laurel
            Trees("Texas Mountain Laurel", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/texas_mountain_laurel_266042203-min.jpeg", "Dermatophyllum secundiflorum", "Tree", "", ""),
            Trees("Texas Mountain Laurel", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/texasmountainlaurelleaf.jpg", "Dermatophyllum secundiflorum", "Tree", "Photo 353834085, (c) Nate Sabo", ""),
            Trees("Texas Mountain Laurel", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/texasmountainlaurelbark.jpg", "Dermatophyllum secundiflorum", "Tree", "Photo 253145635, (c) Chet Burrier", ""),

            # 5. Bald Cypress
            Trees("Bald Cypress", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/bald_cypress_fullsize_1.jpeg", "Taxodium distichum", "Tree", "", ""),
            Trees("Bald Cypress", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/baldcypressleaf.jpeg", "Taxodium distichum", "Tree", "Photo 2795370, (c) Annika Lindqvist", ""),
            Trees("Bald Cypress", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/baldcypressbark.jpg", "Taxodium distichum", "Tree", "Photo 112013391, (c) Laura Clark", ""),

            # 6. Honey Mesquite
            Trees("Honey Mesquite", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/HoneyMesquitefull.jpg", "Prosopis glandulosa", "Tree", "Photo 101224092, (c) CK2AZ", ""),
            Trees("Honey Mesquite", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/HoneyMesquiteleaf.jpg", "Prosopis glandulosa", "Tree", "Photo 302039208, (c) Catherine C. Galley", ""),
            Trees("Honey Mesquite", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/HoneyMesquitebark.jpg", "Prosopis glandulosa", "Tree", "Photo 347954968, (c) John Rosford", ""),

            # 7. Cedar Elm
            Trees("Cedar Elm", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/cedar_elm_71342713-min.jpeg", "Ulmus crassifolia", "Tree", "", ""),
            Trees("Cedar Elm", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/cedar_elm_leaf1.jpeg", "Ulmus crassifolia", "Tree", "", ""),
            Trees("Cedar Elm", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/cedar_elm_bark.jpeg", "Ulmus crassifolia", "Tree", "", ""),

            # 8. Southern Magnolia
            Trees("Southern Magnolia", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/southern_magnolia_246625979-min.jpeg", "Magnolia grandiflora", "Tree", "", ""),
            Trees("Southern Magnolia", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/SouthernMagnolialeaf.jpg", "Magnolia grandiflora", "Tree", "Photo 551360474, (c) Lex Joy", ""),
            Trees("Southern Magnolia", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/SouthernMagnoliabark.jpg", "Magnolia grandiflora", "Tree", "Photo 59481073, (c) Cody Stricker", ""),

            # 9. Loblolly Pine
            Trees("Loblolly Pine", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/loblolly_pine_168861849-min.jpeg", "Pinus taeda", "Tree", "", ""),
            Trees("Loblolly Pine", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/LoblollyPineLeaf.jpg", "Pinus taeda", "Tree", "Photo 402210467, (c) LBuffum", ""),
            Trees("Loblolly Pine", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/LoblollyPineBark.jpg", "Pinus taeda", "Tree", "Photo 109679762, (c) Sophia K", ""),

            # 10. Texas Redbud
            Trees("Texas Redbud", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/Texas+Redbudfull.jpeg", "Cercis canadensis var. texensis", "Tree", "Photo 477364441, (c) Reid Hardin", ""),
            Trees("Texas Redbud", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/Texas+Redbudleaf.jpeg", "Cercis canadensis var. texensis", "Tree", "Photo 479457708, (c) Michelle W.", ""),
            Trees("Texas Redbud", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/Texas+Redbudbark.jpg", "Cercis canadensis var. texensis", "Tree", "Photo 161207149, (c) Kane Sandoval", ""),

            # 11. Crape Myrtle
            Trees("Crape Myrtle", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/Crape+Myrtlefull.jpeg", "Lagerstroemia indica", "Tree", "Photo 463065934, (c) Gonzalo Romero", ""),
            Trees("Crape Myrtle", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/Crape+MyrtleLeaf.jpg", "Lagerstroemia indica", "Tree", "Photo 144113548, (c) Michael Meiring", ""),
            Trees("Crape Myrtle", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/Crape+MyrtleBark.jpeg", "Lagerstroemia indica", "Tree", "Photo 463065959, (c) Gonzalo Romero", ""),

            # 12. Ashe Juniper
            Trees("Ashe Juniper", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/Ashe+JuniperFull.jpg", "Juniperus ashei", "Tree", "Photo 78970594, (c) Gary Rogers", ""),
            Trees("Ashe Juniper", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/Ashe+JuniperLeaf.jpg", "Juniperus ashei", "Tree", "Photo 54313324, (c) Sophia K", ""),
            Trees("Ashe Juniper", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/Ashe+JuniperBark.jpg", "Juniperus ashei", "Tree", "Photo 56893555, (c) Sophia K", ""),

            # 13. Post Oak
            Trees("Post Oak", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/post_oak_69964216-min.jpeg", "Quercus stellata", "Tree", "", ""),
            Trees("Post Oak", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/Post+OakLeaf.jpeg", "Quercus stellata", "Tree", "Photo 236627108, (c) Jo Roberts", ""),
            Trees("Post Oak", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/Post+OakBark.jpg", "Quercus stellata", "Tree", "Photo 171628620, (c) CK2AZ", ""),

            # 14. Bur Oak
            Trees("Bur Oak", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/Bur+OakFull.jpg", "Quercus macrocarpa", "Tree", "Photo 325917393, (c) ashleyrsteel", ""),
            Trees("Bur Oak", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/Bur+OakLeaf.jpeg", "Quercus macrocarpa", "Tree", "Photo 52557659, (c) Lauren McLaurin", ""),
            Trees("Bur Oak", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/Bur+OakBark.jpeg", "Quercus macrocarpa", "Tree", "Photo 431246298, (c) Nikokin", ""),

            # 15. Shumard Oak
            Trees("Shumard Oak", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/Shumard+OakFull.jpeg", "Quercus shumardii", "Tree", "Photo 444034282, (c) hr_dragonfly", ""),
            Trees("Shumard Oak", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/Shumard+OakLeaf.jpg", "Quercus shumardii", "Tree", "Photo 326019601, (c) Jaime González", ""),
            Trees("Shumard Oak", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/Shumard+OakBark.jpg", "Quercus shumardii", "Tree", "Photo 169894479, (c) Brand R", ""),

            # 16. Desert Willow
            Trees("Desert Willow", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/Desert+WillowFull.jpg", "Chilopsis linearis", "Tree", "Photo 521683719, (c) Joseph Aubert", ""),
            Trees("Desert Willow", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/Desert+WillowLeaf.jpeg", "Chilopsis linearis", "Tree", "Photo 383980503, (c) William Harmon", ""),
            Trees("Desert Willow", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/Desert+WillowBark.jpeg", "Chilopsis linearis", "Tree", "Photo 2092453, (c) Laura Clark", ""),

            # 17. Retama
            Trees("Mexican Palo Verde", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/Mexican+Palo+VerdeFull.jpg", "Parkinsonia aculeata", "Tree", "Photo 590612997, (c) Clifton Ladd, C.W.B.", ""),
            Trees("Mexican Palo Verde", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/Mexican+Palo+VerdeLeaf.jpg", "Parkinsonia aculeata", "Tree", "Photo 194536754, (c) Salem De La Luna", ""),
            Trees("Mexican Palo Verde", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/Mexican+Palo+VerdeBark.jpeg", "Parkinsonia aculeata", "Tree", "Photo 467919169, (c) Nicole", ""),

            # 18. Texas Ash
            Trees("Texas Ash", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/texas_ash_947070-min.jpeg", "Fraxinus texensis", "Tree", "", ""),
            Trees("Texas Ash", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/Texas+AshLeaf.jpeg", "Fraxinus texensis", "Tree", "Photo 282523696, (c) saltyhiker", ""),
            Trees("Texas Ash", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/Texas+AshBark.jpg ", "Fraxinus texensis", "Tree", "Photo 20708098, (c) markluffel", ""),

            # 19. Yaupon Holly
            Trees("Yaupon Holly", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/Yaupon+HollyFull.jpeg", "Ilex vomitoria", "Tree", "Photo 451918713, (c) Linda Jo Conn", ""),
            Trees("Yaupon Holly", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/Yaupon+HollyLeaf.jpg", "Ilex vomitoria", "Tree", "Photo 344718632, (c) Lauren McLaurin", ""),
            # Trees("Yaupon Holly", "bark", "", "Ilex vomitoria", "Tree", "", ""),

            # 20. Sweetgum
            Trees("Sweetgum", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/SweetgumFull.jpeg", "Liquidambar styraciflua", "Tree", "Photo 15390772, (c) Sam Kieschnick", ""),
            Trees("Sweetgum", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/SweetgumLeaf.jpeg", "Liquidambar styraciflua", "Tree", "Photo 333665151, (c) Eleanor Pate", ""),
            Trees("Sweetgum", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/SweetgumBark.jpg", "Liquidambar styraciflua", "Tree", "Photo 121477230, (c) Cassidy Best", ""),

            # # 21. Eastern Redcedar
            # Trees("Eastern Redcedar", "close_fullsize", "", "Juniperus virginiana", "Tree", "", ""),
            # Trees("Eastern Redcedar", "leaf", "", "Juniperus virginiana", "Tree", "", ""),
            # Trees("Eastern Redcedar", "bark", "", "Juniperus virginiana", "Tree", "", ""),

            # # 22. Mexican Plum
            # Trees("Mexican Plum", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/mexican_plum_44227239-min.jpeg", "Prunus mexicana", "Tree", "", ""),
            # Trees("Mexican Plum", "leaf", "", "Prunus mexicana", "Tree", "", ""),
            # Trees("Mexican Plum", "bark", "", "Prunus mexicana", "Tree", "", ""),

            # # 23. Hackberry
            # Trees("Hackberry", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/hackberry_324208578-min.jpeg", "Celtis occidentalis", "Tree", "", ""),
            # Trees("Hackberry", "leaf", "", "Celtis occidentalis", "Tree", "", ""),
            # Trees("Hackberry", "bark", "", "Celtis occidentalis", "Tree", "", ""),

            # # 24. Sugarberry
            # Trees("Sugarberry", "close_fullsize", "", "Celtis laevigata", "Tree", "", ""),
            # Trees("Sugarberry", "leaf", "", "Celtis laevigata", "Tree", "", ""),
            # Trees("Sugarberry", "bark", "", "Celtis laevigata", "Tree", "", ""),

            # 25. Texas Persimmon
            Trees("Texas Persimmon", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/Texas_persimmon_full_1.jpeg", "Diospyros texana", "Tree", "", ""),
            Trees("Texas Persimmon", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/Texas_persimmon_leaf_1.jpeg", "Diospyros texana", "Tree", "", ""),
            Trees("Texas Persimmon", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/Texas_persimmon_bark_1.jpeg", "Diospyros texana", "Tree", "", ""),

            # # 26. American Sycamore
            # Trees("American Sycamore", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/american_sycamore_84788584-min.jpeg", "Platanus occidentalis", "Tree", "", ""),
            # Trees("American Sycamore", "leaf", "", "Platanus occidentalis", "Tree", "", ""),
            # Trees("American Sycamore", "bark", "", "Platanus occidentalis", "Tree", "", ""),

            # # 27. Eastern Cottonwood
            # Trees("Eastern Cottonwood", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/cottonwood_68252199-min.jpeg", "Populus deltoides", "Tree", "", ""),
            # Trees("Eastern Cottonwood", "leaf", "", "Populus deltoides", "Tree", "", ""),
            # Trees("Eastern Cottonwood", "bark", "", "Populus deltoides", "Tree", "", ""),

            # # 28. Black Walnut
            # Trees("Black Walnut", "close_fullsize", "", "Juglans nigra", "Tree", "", ""),
            # Trees("Black Walnut", "leaf", "", "Juglans nigra", "Tree", "", ""),
            # Trees("Black Walnut", "bark", "", "Juglans nigra", "Tree", "", ""),

            # # 29. Chinquapin Oak
            # Trees("Chinquapin Oak", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/chinkapin_oak_165800321-min.jpeg", "Quercus muehlenbergii", "Tree", "", ""),
            # Trees("Chinquapin Oak", "leaf", "", "Quercus muehlenbergii", "Tree", "", ""),
            # Trees("Chinquapin Oak", "bark", "", "Quercus muehlenbergii", "Tree", "", ""),

            # # 30. Blackjack Oak
            # Trees("Blackjack Oak", "close_fullsize", "", "Quercus marilandica", "Tree", "", ""),
            # Trees("Blackjack Oak", "leaf", "", "Quercus marilandica", "Tree", "", ""),
            # Trees("Blackjack Oak", "bark", "", "Quercus marilandica", "Tree", "", ""),

            # 31. Anacua
            Trees("Anacua", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/AnacuaFull.jpg", "Ehretia anacua", "Tree", "Photo 362884467, (c) Adam Cohen", ""),
            Trees("Anacua", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/AnacuaLeaf.jpg", "Ehretia anacua", "Tree", "Photo 374520768, (c) Jane Weeden", ""),
            Trees("Anacua", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/AnacuaBark.jpg", "Ehretia anacua", "Tree", "", "Photo 162295170, (c) Kane Sandoval"),

            # # 32. Texas Pistache
            # Trees("Texas Pistache", "close_fullsize", "", "Pistacia texana", "Tree", "", ""),
            # Trees("Texas Pistache", "leaf", "", "Pistacia texana", "Tree", "", ""),
            # Trees("Texas Pistache", "bark", "", "Pistacia texana", "Tree", "", ""),

            # # 33. Texas Ebony
            # Trees("Texas Ebony", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/texas_ebony_2279225-min.jpeg", "Ebenopsis ebano", "Tree", "", ""),
            # Trees("Texas Ebony", "leaf", "", "Ebenopsis ebano", "Tree", "", ""),
            # Trees("Texas Ebony", "bark", "", "Ebenopsis ebano", "Tree", "", ""),

            # # 34. Huisache
            # Trees("Huisache", "close_fullsize", "", "Vachellia farnesiana", "Tree", "", ""),
            # Trees("Huisache", "leaf", "", "Vachellia farnesiana", "Tree", "", ""),
            # Trees("Huisache", "bark", "", "Vachellia farnesiana", "Tree", "", ""),

            # # 35. Guajillo
            # Trees("Guajillo", "close_fullsize", "", "Senegalia berlandieri", "Tree", "", ""),
            # Trees("Guajillo", "leaf", "", "Senegalia berlandieri", "Tree", "", ""),
            # Trees("Guajillo", "bark", "", "Senegalia berlandieri", "Tree", "", ""),

            # # 36. Goldenball Leadtree
            # Trees("Goldenball Leadtree", "close_fullsize", "", "Leucaena retusa", "Tree", "", ""),
            # Trees("Goldenball Leadtree", "leaf", "", "Leucaena retusa", "Tree", "", ""),
            # Trees("Goldenball Leadtree", "bark", "", "Leucaena retusa", "Tree", "", ""),

            # # 37. Texas Madrone
            # Trees("Texas Madrone", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/texas_madrone_347099237-min.jpeg", "Arbutus xalapensis", "Tree", "", ""),
            # Trees("Texas Madrone", "leaf", "", "Arbutus xalapensis", "Tree", "", ""),
            # Trees("Texas Madrone", "bark", "", "Arbutus xalapensis", "Tree", "", ""),

            # # 38. Chisos Red Oak
            # Trees("Chisos Red Oak", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/texas_red_oak_85298162-min.jpeg", "Quercus gravesii", "Tree", "", ""),
            # Trees("Chisos Red Oak", "leaf", "", "Quercus gravesii", "Tree", "", ""),
            # Trees("Chisos Red Oak", "bark", "", "Quercus gravesii", "Tree", "", ""),

            # # 39. Bigtooth Maple
            # Trees("Bigtooth Maple", "close_fullsize", "", "Acer grandidentatum", "Tree", "", ""),
            # Trees("Bigtooth Maple", "leaf", "", "Acer grandidentatum", "Tree", "", ""),
            # Trees("Bigtooth Maple", "bark", "", "Acer grandidentatum", "Tree", "", ""),

            # # 40. Red Maple
            # Trees("Red Maple", "close_fullsize", "", "Acer rubrum", "Tree", "", ""),
            # Trees("Red Maple", "leaf", "", "Acer rubrum", "Tree", "", ""),
            # Trees("Red Maple", "bark", "", "Acer rubrum", "Tree", "", ""),

            # # 41. Mexican Buckeye
            # Trees("Mexican Buckeye", "close_fullsize", "", "Ungnadia speciosa", "Tree", "", ""),
            # Trees("Mexican Buckeye", "leaf", "", "Ungnadia speciosa", "Tree", "", ""),
            # Trees("Mexican Buckeye", "bark", "", "Ungnadia speciosa", "Tree", "", ""),

            # # 42. Carolina Basswood
            # Trees("Carolina Basswood", "close_fullsize", "", "Tilia americana var. caroliniana", "Tree", "", ""),
            # Trees("Carolina Basswood", "leaf", "", "Tilia americana var. caroliniana", "Tree", "", ""),
            # Trees("Carolina Basswood", "bark", "", "Tilia americana var. caroliniana", "Tree", "", ""),

            # 43. Rusty Blackhaw
            Trees("Rusty Blackhaw", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/Rusty+BlackhawFull.jpg", "Viburnum rufidulum", "Tree", "Photo 64043896, (c) Sam Kieschnick", ""),
            Trees("Rusty Blackhaw", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/Rusty+BlackhawLeaf.jpg", "Viburnum rufidulum", "Tree", "Photo 358268337, (c) Libby Aragon", ""),
            Trees("Rusty Blackhaw", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/Rusty+BlackhawBark.jpeg", "Viburnum rufidulum", "Tree", "Photo 118435303, (c) Michelle W.", ""),

            # # 44. Two-wing Silverbell
            # Trees("Two-wing Silverbell", "close_fullsize", "", "Halesia diptera", "Tree", "", ""),
            # Trees("Two-wing Silverbell", "leaf", "", "Halesia diptera", "Tree", "", ""),
            # Trees("Two-wing Silverbell", "bark", "", "Halesia diptera", "Tree", "", ""),

            # # 45. Flowering Dogwood
            # Trees("Flowering Dogwood", "close_fullsize", "", "Cornus florida", "Tree", "", ""),
            # Trees("Flowering Dogwood", "leaf", "", "Cornus florida", "Tree", "", ""),
            # Trees("Flowering Dogwood", "bark", "", "Cornus florida", "Tree", "", ""),

            # # 46. Longleaf Pine
            # Trees("Longleaf Pine", "close_fullsize", "", "Pinus palustris", "Tree", "", ""),
            # Trees("Longleaf Pine", "leaf", "", "Pinus palustris", "Tree", "", ""),
            # Trees("Longleaf Pine", "bark", "", "Pinus palustris", "Tree", "", ""),

            # # 47. Shortleaf Pine
            # Trees("Shortleaf Pine", "close_fullsize", "", "Pinus echinata", "Tree", "", ""),
            # Trees("Shortleaf Pine", "leaf", "", "Pinus echinata", "Tree", "", ""),
            # Trees("Shortleaf Pine", "bark", "", "Pinus echinata", "Tree", "", ""),

            # # 48. Overcup Oak
            # Trees("Overcup Oak", "close_fullsize", "", "Quercus lyrata", "Tree", "", ""),
            # Trees("Overcup Oak", "leaf", "", "Quercus lyrata", "Tree", "", ""),
            # Trees("Overcup Oak", "bark", "", "Quercus lyrata", "Tree", "", ""),

            # # 49. Water Oak
            # Trees("Water Oak", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/water_oak_11503888-min.jpeg", "Quercus nigra", "Tree", "", ""),
            # Trees("Water Oak", "leaf", "", "Quercus nigra", "Tree", "", ""),
            # Trees("Water Oak", "bark", "", "Quercus nigra", "Tree", "", ""),

            # # 50. Willow Oak
            # Trees("Willow Oak", "close_fullsize", "", "Quercus phellos", "Tree", "", ""),
            # Trees("Willow Oak", "leaf", "", "Quercus phellos", "Tree", "", ""),
            # Trees("Willow Oak", "bark", "", "Quercus phellos", "Tree", "", ""),

            # # 51. American Elm
            # Trees("American Elm", "close_fullsize", "", "Ulmus americana", "Tree", "", ""),
            # Trees("American Elm", "leaf", "", "Ulmus americana", "Tree", "", ""),
            # Trees("American Elm", "bark", "", "Ulmus americana", "Tree", "", ""),

            # # 52. Winged Elm
            # Trees("Winged Elm", "close_fullsize", "", "Ulmus alata", "Tree", "", ""),
            # Trees("Winged Elm", "leaf", "", "Ulmus alata", "Tree", "", ""),
            # Trees("Winged Elm", "bark", "", "Ulmus alata", "Tree", "", ""),

            # 53. Black Cherry
            Trees("Black Cherry", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/Black+CherryFull.jpg", "Prunus serotina", "Tree", "Photo 64562125, (c) Emily Summerbell", ""),
            Trees("Black Cherry", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/Black+CherryLeaf.jpg", "Prunus serotina", "Tree", "Photo 18479136, (c) Laura Clark", ""),
            Trees("Black Cherry", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/Black+CherryBark.jpg", "Prunus serotina", "Tree", "Photo 618804717, (c) Northcut", ""),

            # # 54. Carolina Buckthorn
            # Trees("Carolina Buckthorn", "close_fullsize", "", "Frangula caroliniana", "Tree", "", ""),
            # Trees("Carolina Buckthorn", "leaf", "", "Frangula caroliniana", "Tree", "", ""),
            # Trees("Carolina Buckthorn", "bark", "", "Frangula caroliniana", "Tree", "", ""),

            # # 55. Common Buttonbush
            # Trees("Common Buttonbush", "close_fullsize", "", "Cephalanthus occidentalis", "Tree", "", ""),
            # Trees("Common Buttonbush", "leaf", "", "Cephalanthus occidentalis", "Tree", "", ""),
            # Trees("Common Buttonbush", "bark", "", "Cephalanthus occidentalis", "Tree", "", ""),

            # # 56. Green Ash
            # Trees("Green Ash", "close_fullsize", "", "Fraxinus pennsylvanica", "Tree", "", ""),
            # Trees("Green Ash", "leaf", "", "Fraxinus pennsylvanica", "Tree", "", ""),
            # Trees("Green Ash", "bark", "", "Fraxinus pennsylvanica", "Tree", "", ""),

            # # 57. White Ash
            # Trees("White Ash", "close_fullsize", "", "Fraxinus americana", "Tree", "", ""),
            # Trees("White Ash", "leaf", "", "Fraxinus americana", "Tree", "", ""),
            # Trees("White Ash", "bark", "", "Fraxinus americana", "Tree", "", ""),

            # # 58. Texas Mulberry
            # Trees("Texas Mulberry", "close_fullsize", "", "Morus microphylla", "Tree", "", ""),
            # Trees("Texas Mulberry", "leaf", "", "Morus microphylla", "Tree", "", ""),
            # Trees("Texas Mulberry", "bark", "", "Morus microphylla", "Tree", "", ""),

            # 59. Red Mulberry
            Trees("Red Mulberry", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/Red+MulberryFull.jpg", "Morus rubra", "Tree", "Photo 186577373, (c) Sam Kieschnick", ""),
            Trees("Red Mulberry", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/Red+MulberryLeaf.jpeg", "Morus rubra", "Tree", "Photo 371438844, (c) Mike Tilley", ""),
            Trees("Red Mulberry", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/Red+MulberryBark.jpg", "Morus rubra", "Tree", "Photo 93803054, (c) Brand R", ""),

            # 60. Sassafras
            Trees("Sassafras", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/SassafrasFull.jpg", "Sassafras albidum", "Tree", "Photo 167737857, (c) Northcut", ""),
            Trees("Sassafras", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/SassafrasLeaf.jpeg", "Sassafras albidum", "Tree", "Photo 194523029, (c) Reid Hardin", ""),
            Trees("Sassafras", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/SassafrasBark.jpg", "Sassafras albidum", "Tree", "Photo 167472690, (c) Sandy Wolkenberg", "")
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

        # # --- FLOWERS (Top 15) ---
        # flowers = [
        #     Flowers("Texas Bluebonnet", "close_fullsize", "", "Lupinus texensis", "Flower", "", ""),
        #     Flowers("Indian Blanket", "close_fullsize", "", "Gaillardia pulchella", "Flower", "", ""),
        #     Flowers("Pink Evening Primrose", "close_fullsize", "", "Oenothera speciosa", "Flower", "", ""),
        #     Flowers("Black-eyed Susan", "close_fullsize", "", "Rudbeckia hirta", "Flower", "", ""),
        #     Flowers("Mexican Hat", "close_fullsize", "", "Ratibida columnifera", "Flower", "", ""),
        #     Flowers("Texas Paintbrush", "close_fullsize", "", "Castilleja indivisa", "Flower", "", ""),
        #     Flowers("Plains Coreopsis", "close_fullsize", "", "Coreopsis tinctoria", "Flower", "", ""),
        #     Flowers("Drummond Phlox", "close_fullsize", "", "Phlox drummondii", "Flower", "", ""),
        #     Flowers("Texas Bluebell", "close_fullsize", "", "Eustoma exaltatum", "Flower", "", ""),
        #     Flowers("Purple Coneflower", "close_fullsize", "", "Echinacea purpurea", "Flower", "", ""),
        #     Flowers("Common Sunflower", "close_fullsize", "", "Helianthus annuus", "Flower", "", ""),
        #     Flowers("Winecup", "close_fullsize", "", "Callirhoe involuta", "Flower", "", ""),
        #     Flowers("Texas Lantana", "close_fullsize", "", "Lantana urticoides", "Flower", "", ""),
        #     Flowers("Standing Cypress", "close_fullsize", "", "Ipomopsis rubra", "Flower", "", ""),
        #     Flowers("Blue-eyed Grass", "close_fullsize", "", "Sisyrinchium campestre", "Flower", "", "")
        # ]
        
        for flower in flowers:
            exists = Flowers.query.filter_by(plant_name=flower.plant_name).first()
            if not exists:
                db.session.add(flower)

        # --- VINES (Top 10) ---
        vines = [
            Vines("Mustang Grape", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/vines/Mustang+Grape.jpeg", "Vitis mustangensis", "Vine", "Photo 105715542, (c) Michael D Fox", ""),
            Vines("Crossvine", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/vines/Crossvine.jpg", "Bignonia capreolata", "Vine", "Photo 117496938, (c) Victor Engel", ""),
            Vines("Virginia Creeper", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/vines/Virginia+Creeper.jpeg", "Parthenocissus quinquefolia", "Vine", "Photo 400071639, (c) Annika Lindqvist", ""),
            Vines("Coral Honeysuckle", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/vines/Coral+Honeysuckle.jpeg", "Lonicera sempervirens", "Vine", "Photo 32879402, (c) Cleveland Powell", ""),
            Vines("Coral Honeysuckle", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/vines/Coral+Honeysuckle.jpg", "Lonicera sempervirens", "Vine", "Photo 64177888, (c) Luke Padon", ""),
            Vines("Trumpet Vine", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/vines/Trumpet+Vine.jpg", "Campsis radicans", "Vine", "Photo 542404490, (c) Eleanor Pate", ""),
            Vines("Trumpet Vine", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/vines/Trumpet+Vine2.jpg", "Campsis radicans", "Vine", "Photo 578614577, (c) Terry Woodward", ""),
            Vines("Purple Passionflower", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/vines/Purple+Passionflower.jpeg", "Passiflora incarnata", "Vine", "Photo 7256352, (c) Laura Clark", ""),
            Vines("Poison Ivy", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/vines/Poison+Ivy.jpeg", "Toxicodendron radicans", "Vine", "Photo 117669617, (c) Blake Bringhurst", ""),
            Vines("Poison Ivy", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/vines/Poison+Ivy.jpg", "Toxicodendron radicans", "Vine", "Photo 66178058, (c) Sam Kieschnick", ""),
            Vines("Poison Ivy", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/vines/Poison+Ivy2.jpg", "Toxicodendron radicans", "Vine", "Photo 66454547, (c) Tyler Cannon", ""),
            Vines("Poison Ivy", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/vines/Poison+Ivy3.jpeg", "Toxicodendron radicans", "Vine", "Photo 485684538, (c) Nathan Walther", ""),
            Vines("Yellow Jessamine", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/vines/Yellow+Jessamine.jpeg", "Gelsemium sempervirens", "Vine", "Photo 3104620, (c) Laura Clark", ""),
            Vines("Yellow Jessamine", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/vines/Yellow+Jessamine.jpg", "Gelsemium sempervirens", "Vine", "Photo 260571170, (c) Mike Duran", ""),
            Vines("Southern Dewberry", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/vines/Southern+Dewberry.jpeg", "Rubus trivialis", "Vine", "Photo 188175195, (c) saltyhiker", ""),
            Vines("Southern Dewberry", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/vines/Southern+Dewberry.jpg", "Rubus trivialis", "Vine", "Photo 649072050, (c) Trey Philips", ""),
            Vines("Peppervine", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/vines/Peppervine.jpeg", "Nekemias arborea", "Vine", "Photo 226769569, (c) Annika Lindqvist", "")
        ]
        
        for vine in vines:
            exists = Vines.query.filter_by(plant_name=vine.plant_name).first()
            if not exists:
                db.session.add(vine)

        # --- CACTI (Top 10) ---
        cacti = [
            Cacti("Texas Prickly Pear", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/cacti/Prickly+Pear.jpeg", "Opuntia engelmannii", "Cactus", "Photo 373090621, (c) Suanne Pyle", ""),
            Cacti("Lace Hedgehog", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/cacti/Lace+Hedgehog.jpeg", "Echinocereus reichenbachii", "Cactus", "Photo 366998561, (c) Reid Hardin", ""),
            Cacti("Horse Crippler", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/cacti/Horse+Crippler.jpeg", "Echinocactus texensis", "Cactus", "Photo 284772979, (c) Charlie Meador", ""),
            Cacti("Kingcup Cactus", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/cacti/Kingcup+Cactus.jpeg", "Echinocereus triglochidiatus", "Cactus", "Photo 7993799, (c) Annika Lindqvist", ""),
            Cacti("Nipple Cactus", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/cacti/Nipple+Cactus.jpeg", "Mammillaria heyderi", "Cactus", "Photo 268259456, (c) Michelle W. ", ""),
            Cacti("Tasajillo", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/cacti/Tasajillo.jpg", "Cylindropuntia leptocaulis", "Cactus", "Photo 646641075, (c) Nathan Aaron", ""),
            Cacti("Blind Prickly Pear", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/cacti/Blind+Prickly+Pear.jpeg", "Opuntia rufida", "Cactus", "Photo 123040724, (c) Reid Hardin", ""),
            Cacti("Strawberry Cactus", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/cacti/Strawberry+Cactus.jpeg", "Echinocereus stramineus", "Cactus", "Photo 284982536, (c) Michelle W.", ""),
            Cacti("Texas Rainbow Cactus", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/cacti/Rainbow+Cactus.jpg", "Echinocereus dasyacanthus", "Cactus", "Photo 410792920, (c) Nick Block", ""),
            Cacti("Tree Cholla", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/cacti/Tree+Cholla.jpg", "Cylindropuntia imbricata", "Cactus", "Photo 106532453, (c) CK2AZ", "")
        ]
        
        for cactus in cacti:
            exists = Cacti.query.filter_by(plant_name=cactus.plant_name).first()
            if not exists:
                db.session.add(cactus)

        # --- GRASSES (Top 10) ---
        grasses = [
            Grasses("Buffalo Grass", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/grasses/Buffalo+Grass.jpeg", "Bouteloua dactyloides", "Grass", "Photo 123265962, (c) saltyhiker", ""),
            Grasses("Little Bluestem", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/grasses/Little+Bluestem.jpg", "Schizachyrium scoparium", "Grass", "Photo 344718541, (c) Lauren McLaurin", ""),
            Grasses("Big Bluestem", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/grasses/Big+Bluestem.jpeg", "Andropogon gerardii", "Grass", "Photo 230582693, (c) Catherine C. Galley", ""),
            Grasses("Indiangrass", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/grasses/Indiangrass.jpeg", "Sorghastrum nutans", "Grass", "Photo 10860598, (c) Annika Lindqvist", ""),
            Grasses("Switchgrass", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/grasses/Switchgrass.jpg", "Panicum virgatum", "Grass", "Photo 590555846, (c) Dustin Snider", ""),
            Grasses("Sideoats Grama", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/grasses/Sideoats+Grama.jpeg", "Bouteloua curtipendula", "Grass", "Photo 426529007, (c) Anders Hastings", ""),
            Grasses("Blue Grama", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/grasses/Blue+Grama.jpg", "Bouteloua gracilis", "Grass", "Photo 432159307, (c) Dominic Gentilcore", ""),
            Grasses("Texas Wintergrass", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/grasses/Texas+Wintergrass.jpeg", "Nassella leucotricha", "Grass", "Photo 37419762, (c) Annika Lindqvist", ""),
            Grasses("River Oats", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/grasses/River+Oats.jpg", "Chasmanthium latifolium", "Grass", "Photo 610161286, (c) Texas Bird Family", ""),
            Grasses("Hairawn Muhly", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/grasses/Hairawn+Muhly.jpeg", "Muhlenbergia capillaris", "Grass", "Photo 102657833, (c) Dan Johnson", "")
        ]
        
        for grass in grasses:
            exists = Grasses.query.filter_by(plant_name=grass.plant_name).first()
            if not exists:
                db.session.add(grass)

        # --- AQUATIC (Top 10) ---
        aquatic = [
            Aquatic("White Water Lily", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/flowers/White+Water+Lily.jpeg", "Nymphaea odorata", "Aquatic", "Photo 140306027, (c) Annika Lindqvist", ""),
            Aquatic("American Lotus", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/flowers/American+Lotus.jpg", "Nelumbo lutea", "Aquatic", "Photo 47140810, (c) Laura Clark", ""),
            Aquatic("Pickerelweed", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/flowers/Pickerelweed.jpg", "Pontederia cordata", "Aquatic", "Photo 28931819, (c) Rich Sommer", ""),
            Aquatic("Common Duckweed", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/aquatic/Common+Duckweed.jpg", "Lemna minor", "Aquatic", "Photo 49914507, (c) Attila Oláh", ""),
            Aquatic("Coontail", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/aquatic/Coontail.jpeg", "Ceratophyllum demersum", "Aquatic", "Photo 193786804, (c) chiuluan", ""),
            Aquatic("Water Hyacinth", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/aquatic/Water+Hyacinth.jpg", "Eichhornia crassipes", "Aquatic", "Photo 366398988, (c) Terry Woodward", ""),
            Aquatic("Broadleaf Arrowhead", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/aquatic/Broadleaf+Arrowhead.jpeg", "Sagittaria latifolia", "Aquatic", "Photo 30424581, (c) eamonccorbett", ""),
            Aquatic("Spatterdock", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/aquatic/Spatterdock.jpeg", "Nuphar advena", "Aquatic", "Photo 182355520, (c) gpete", ""),
            Aquatic("Water Pennywort", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/aquatic/Water+Pennywort.jpeg", "Hydrocotyle umbellata", "Aquatic", "Photo 299878899, (c) Michelle W.", ""),
            Aquatic("Southern Waternymph", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/aquatic/Southern+Waternymph.jpeg", "Najas guadalupensis", "Aquatic", "Photo 287296223, (c) Michael J. Papay", "")
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