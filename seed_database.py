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
            Trees('Yaupon Holly', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/yaupon_holly_inat_175054829_w960_q80_fb043b79b90a.webp', 'Ilex vomitoria', 'Tree', 'iNaturalist Photo 175054829; CC0; observer: Nonbinary-Naturalist; https://www.inaturalist.org/photos/175054829; CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # 20. Sweetgum
            Trees("Sweetgum", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/SweetgumFull.jpeg", "Liquidambar styraciflua", "Tree", "Photo 15390772, (c) Sam Kieschnick", ""),
            Trees("Sweetgum", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/SweetgumLeaf.jpeg", "Liquidambar styraciflua", "Tree", "Photo 333665151, (c) Eleanor Pate", ""),
            Trees("Sweetgum", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/SweetgumBark.jpg", "Liquidambar styraciflua", "Tree", "Photo 121477230, (c) Cassidy Best", ""),

            # # 21. Eastern Redcedar
            Trees('Eastern Redcedar', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/eastern_redcedar_inat_421841207_w960_q80_9052ee05e853.webp', 'Juniperus virginiana', 'Tree', 'iNaturalist Photo 421841207; (c) Mason Holum, some rights reserved (CC BY); https://www.inaturalist.org/photos/421841207; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Eastern Redcedar', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/eastern_redcedar_inat_342600623_w960_q80_9ea3bbd42aa8.webp', 'Juniperus virginiana', 'Tree', 'iNaturalist Photo 342600623; (c) John Baur, some rights reserved (CC BY); https://www.inaturalist.org/photos/342600623; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Eastern Redcedar', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/eastern_redcedar_inat_352652345_w960_q80_44206b24900d.webp', 'Juniperus virginiana', 'Tree', 'iNaturalist Photo 352652345; (c) Laura Clark, some rights reserved (CC BY); https://www.inaturalist.org/photos/352652345; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 22. Mexican Plum
            Trees('Mexican Plum', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/mexican_plum_inat_7315246_w960_q80_101032841877.webp', 'Prunus mexicana', 'Tree', 'iNaturalist Photo 7315246; (c) Sam Kieschnick, some rights reserved (CC BY); https://www.inaturalist.org/photos/7315246; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Mexican Plum', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/mexican_plum_inat_3823777_w960_q80_435bd41fd772.webp', 'Prunus mexicana', 'Tree', 'iNaturalist Photo 3823777; (c) Sam Kieschnick, some rights reserved (CC BY); https://www.inaturalist.org/photos/3823777; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Mexican Plum', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/mexican_plum_inat_183504508_w960_q80_c760bc4d567a.webp', 'Prunus mexicana', 'Tree', 'iNaturalist Photo 183504508; (c) Michelle W. （鍾偉瑋）, some rights reserved (CC BY); https://www.inaturalist.org/photos/183504508; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 23. Hackberry
            Trees('Hackberry', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/hackberry_inat_320020321_w960_q80_15cb7fd8286a.webp', 'Celtis occidentalis', 'Tree', 'iNaturalist Photo 320020321; (c) M. Whitson, some rights reserved (CC BY); https://www.inaturalist.org/photos/320020321; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Hackberry', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/hackberry_inat_549148697_w960_q80_335ecd5e0112.webp', 'Celtis occidentalis', 'Tree', 'iNaturalist Photo 549148697; (c) Tom Pollard, some rights reserved (CC BY); https://www.inaturalist.org/photos/549148697; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Hackberry', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/hackberry_inat_599584881_w960_q80_cee552469a50.webp', 'Celtis occidentalis', 'Tree', 'iNaturalist Photo 599584881; CC0; observer: Terri Koontz; https://www.inaturalist.org/photos/599584881; CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 24. Sugarberry
            Trees('Sugarberry', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/sugarberry_inat_2406402_w960_q80_0e55ec09eed8.webp', 'Celtis laevigata', 'Tree', 'iNaturalist Photo 2406402; (c) Nick Mirro, some rights reserved (CC BY); https://www.inaturalist.org/photos/2406402; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Sugarberry', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/sugarberry_inat_91922829_w960_q80_7040047fd125.webp', 'Celtis laevigata', 'Tree', 'iNaturalist Photo 91922829; (c) Cody Stricker, some rights reserved (CC BY); https://www.inaturalist.org/photos/91922829; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Sugarberry', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/sugarberry_inat_375437947_w960_q80_bf06f9781b8b.webp', 'Celtis laevigata', 'Tree', 'iNaturalist Photo 375437947; CC0; observer: lanechaffin; https://www.inaturalist.org/photos/375437947; CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # 25. Texas Persimmon
            Trees("Texas Persimmon", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/Texas_persimmon_full_1.jpeg", "Diospyros texana", "Tree", "", ""),
            Trees("Texas Persimmon", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/Texas_persimmon_leaf_1.jpeg", "Diospyros texana", "Tree", "", ""),
            Trees("Texas Persimmon", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/Texas_persimmon_bark_1.jpeg", "Diospyros texana", "Tree", "", ""),

            # 26. American Sycamore
            Trees("American Sycamore", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/American+SycamoreFull.jpeg", "Platanus occidentalis", "Tree", "Photo 24146205, (c) Sam Kieschnick", ""),
            Trees("American Sycamore", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/American+SycamoreLeaf.jpeg", "Platanus occidentalis", "Tree", "Photo 484004792, (c) saltyhiker", ""),
            Trees("American Sycamore", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/American+SycamoreBark.jpeg", "Platanus occidentalis", "Tree", "Photo 36914582, (c) Annika Lindqvist", ""),

            # # 27. Eastern Cottonwood
            Trees('Eastern Cottonwood', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/eastern_cottonwood_inat_1165161_w960_q80_71bdadac07ca.webp', 'Populus deltoides', 'Tree', 'iNaturalist Photo 1165161; CC0; observer: Parker Hopkins; https://www.inaturalist.org/photos/1165161; CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Eastern Cottonwood', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/eastern_cottonwood_inat_208988640_w960_q80_440c43b08507.webp', 'Populus deltoides', 'Tree', 'iNaturalist Photo 208988640; (c) Leila Dasher, some rights reserved (CC BY); https://www.inaturalist.org/photos/208988640; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Eastern Cottonwood', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/eastern_cottonwood_inat_441348113_w960_q80_ac200d0ad11f.webp', 'Populus deltoides', 'Tree', 'iNaturalist Photo 441348113; CC0; observer: Griffin Bray; https://www.inaturalist.org/photos/441348113; CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 28. Black Walnut
            Trees('Black Walnut', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/black_walnut_inat_85826062_w960_q80_62fd7bcda7f5.webp', 'Juglans nigra', 'Tree', 'iNaturalist Photo 85826062; CC0; observer: Reuven Martin; https://www.inaturalist.org/photos/85826062; CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Black Walnut', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/black_walnut_inat_79527820_w960_q80_038133122d93.webp', 'Juglans nigra', 'Tree', 'iNaturalist Photo 79527820; (c) Bob Virag, some rights reserved (CC BY); https://www.inaturalist.org/photos/79527820; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Black Walnut', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/black_walnut_inat_348919748_w960_q80_82e9124d662e.webp', 'Juglans nigra', 'Tree', 'iNaturalist Photo 348919748; (c) Sandy Wolkenberg, some rights reserved (CC BY); https://www.inaturalist.org/photos/348919748; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 29. Chinquapin Oak
            Trees('Chinquapin Oak', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/chinquapin_oak_inat_49622514_w960_q80_d89c220c9f76.webp', 'Quercus muehlenbergii', 'Tree', 'iNaturalist Photo 49622514; (c) naturalist charlie, some rights reserved (CC BY); https://www.inaturalist.org/photos/49622514; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Chinquapin Oak', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/chinquapin_oak_inat_144947700_w960_q80_5190418cb9a3.webp', 'Quercus muehlenbergii', 'Tree', 'iNaturalist Photo 144947700; CC0; observer: Daniel Estabrooks; https://www.inaturalist.org/photos/144947700; CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Chinquapin Oak', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/chinquapin_oak_inat_352794564_w960_q80_8feca2f6b7de.webp', 'Quercus muehlenbergii', 'Tree', 'iNaturalist Photo 352794564; (c) Peyton Phelps, some rights reserved (CC BY); https://www.inaturalist.org/photos/352794564; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 30. Blackjack Oak
            Trees('Blackjack Oak', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/blackjack_oak_inat_631162743_w960_q80_53015bd03b4d.webp', 'Quercus marilandica', 'Tree', 'iNaturalist Photo 631162743; (c) Joshua, some rights reserved (CC BY); https://www.inaturalist.org/photos/631162743; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Blackjack Oak', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/blackjack_oak_inat_270588858_w960_q80_03cfba06fcdd.webp', 'Quercus marilandica', 'Tree', 'iNaturalist Photo 270588858; CC0; observer: Adam Kranz; https://www.inaturalist.org/photos/270588858; CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Blackjack Oak', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/blackjack_oak_inat_626076675_w960_q80_13d174e15c02.webp', 'Quercus marilandica', 'Tree', 'iNaturalist Photo 626076675; (c) Joshua, some rights reserved (CC BY); https://www.inaturalist.org/photos/626076675; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # 31. Anacua
            Trees("Anacua", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/AnacuaFull.jpg", "Ehretia anacua", "Tree", "Photo 362884467, (c) Adam Cohen", ""),
            Trees("Anacua", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/AnacuaLeaf.jpg", "Ehretia anacua", "Tree", "Photo 374520768, (c) Jane Weeden", ""),
            Trees("Anacua", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/AnacuaBark.jpg", "Ehretia anacua", "Tree", "", "Photo 162295170, (c) Kane Sandoval"),

            # # 32. Texas Pistache
            Trees('Texas Pistache', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/texas_pistache_inat_166749214_w960_q80_b71b3811d352.webp', 'Pistacia texana', 'Tree', 'iNaturalist Photo 166749214; (c) Carlos Domínguez-Rodríguez, some rights reserved (CC BY); https://www.inaturalist.org/photos/166749214; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Texas Pistache', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/texas_pistache_inat_507964613_w960_q80_c0d8e131779e.webp', 'Pistacia texana', 'Tree', 'iNaturalist Photo 507964613; (c) Ricardo Jaimes-López, some rights reserved (CC BY); https://www.inaturalist.org/photos/507964613; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Texas Pistache', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/texas_pistache_inat_698071250_w960_q80_b7f394813b22.webp', 'Pistacia texana', 'Tree', 'iNaturalist Photo 698071250; (c) Ulises Pinedo, some rights reserved (CC BY); https://www.inaturalist.org/photos/698071250; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 33. Texas Ebony
            Trees('Texas Ebony', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/texas_ebony_inat_183132714_w960_q80_946ad0c0c293.webp', 'Ebenopsis ebano', 'Tree', 'iNaturalist Photo 183132714; (c) mattmsa, some rights reserved (CC BY); https://www.inaturalist.org/photos/183132714; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Texas Ebony', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/texas_ebony_inat_285319618_w960_q80_bcc5832b3708.webp', 'Ebenopsis ebano', 'Tree', 'iNaturalist Photo 285319618; (c) JHummel, some rights reserved (CC BY); https://www.inaturalist.org/photos/285319618; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Texas Ebony', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/texas_ebony_inat_28181088_w960_q80_80c65381a626.webp', 'Ebenopsis ebano', 'Tree', 'iNaturalist Photo 28181088; (c) Millie Basden, some rights reserved (CC BY); https://www.inaturalist.org/photos/28181088; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 34. Huisache
            Trees('Huisache', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/huisache_inat_184494051_w960_q80_60646aa00dd5.webp', 'Vachellia farnesiana', 'Tree', 'iNaturalist Photo 184494051; (c) Adriana Nelly Correa Sandoval, some rights reserved (CC BY); https://www.inaturalist.org/photos/184494051; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Huisache', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/huisache_inat_301695473_w960_q80_07bf73cdadfc.webp', 'Vachellia farnesiana', 'Tree', 'iNaturalist Photo 301695473; (c) Joseph Aubert, some rights reserved (CC BY); https://www.inaturalist.org/photos/301695473; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Huisache', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/huisache_inat_106826559_w960_q80_0e6c92884c5f.webp', 'Vachellia farnesiana', 'Tree', 'iNaturalist Photo 106826559; (c) Michelle W. （鍾偉瑋）, some rights reserved (CC BY); https://www.inaturalist.org/photos/106826559; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 35. Guajillo
            Trees('Guajillo', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/guajillo_inat_343309576_w960_q80_5ca20082f47a.webp', 'Senegalia berlandieri', 'Tree', 'iNaturalist Photo 343309576; (c) Sam Kieschnick, some rights reserved (CC BY); https://www.inaturalist.org/photos/343309576; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Guajillo', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/guajillo_inat_240366813_w960_q80_676841919b00.webp', 'Senegalia berlandieri', 'Tree', 'iNaturalist Photo 240366813; (c) Jane Weeden, some rights reserved (CC BY); https://www.inaturalist.org/photos/240366813; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Guajillo', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/guajillo_inat_467711585_w960_q80_bdee7ba6ffca.webp', 'Senegalia berlandieri', 'Tree', 'iNaturalist Photo 467711585; (c) Jo Roberts, some rights reserved (CC BY); https://www.inaturalist.org/photos/467711585; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 36. Goldenball Leadtree
            Trees('Goldenball Leadtree', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/goldenball_leadtree_inat_689104544_w960_q80_e9c2d2ce90f0.webp', 'Leucaena retusa', 'Tree', 'iNaturalist Photo 689104544; (c) Jo Roberts, some rights reserved (CC BY); https://www.inaturalist.org/photos/689104544; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Goldenball Leadtree', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/goldenball_leadtree_inat_120290338_w960_q80_351d091287d1.webp', 'Leucaena retusa', 'Tree', 'iNaturalist Photo 120290338; (c) Jo Roberts, some rights reserved (CC BY); https://www.inaturalist.org/photos/120290338; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Goldenball Leadtree', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/goldenball_leadtree_inat_162512456_w960_q80_41c834dd911a.webp', 'Leucaena retusa', 'Tree', 'iNaturalist Photo 162512456; (c) Jo Roberts, some rights reserved (CC BY); https://www.inaturalist.org/photos/162512456; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 37. Texas Madrone
            Trees('Texas Madrone', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/texas_madrone_inat_43954549_w960_q80_831bcc33663e.webp', 'Arbutus xalapensis', 'Tree', 'iNaturalist Photo 43954549; (c) Michelle Lay, some rights reserved (CC BY); https://www.inaturalist.org/photos/43954549; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Texas Madrone', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/texas_madrone_inat_72659982_w960_q80_f70efead5f91.webp', 'Arbutus xalapensis', 'Tree', 'iNaturalist Photo 72659982; (c) Luke Padon, some rights reserved (CC BY); https://www.inaturalist.org/photos/72659982; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Texas Madrone', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/texas_madrone_inat_43954610_w960_q80_970cb5b67dd5.webp', 'Arbutus xalapensis', 'Tree', 'iNaturalist Photo 43954610; (c) Michelle Lay, some rights reserved (CC BY); https://www.inaturalist.org/photos/43954610; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 38. Chisos Red Oak
            Trees('Chisos Red Oak', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/chisos_red_oak_inat_30307304_w960_q80_7bc33c654904.webp', 'Quercus gravesii', 'Tree', 'iNaturalist Photo 30307304; (c) Richard Jacob, some rights reserved (CC BY); https://www.inaturalist.org/photos/30307304; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Chisos Red Oak', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/chisos_red_oak_inat_511764723_w960_q80_d8a48581e1fa.webp', 'Quercus gravesii', 'Tree', 'iNaturalist Photo 511764723; (c) Joseph Aubert, some rights reserved (CC BY); https://www.inaturalist.org/photos/511764723; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Chisos Red Oak', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/chisos_red_oak_inat_275133833_w960_q80_68e8ad4c2d7c.webp', 'Quercus gravesii', 'Tree', 'iNaturalist Photo 275133833; (c) Cody Stricker, some rights reserved (CC BY); https://www.inaturalist.org/photos/275133833; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 39. Bigtooth Maple
            Trees('Bigtooth Maple', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/bigtooth_maple_inat_47784649_w960_q80_9cf5aa6edd21.webp', 'Acer grandidentatum', 'Tree', 'iNaturalist Photo 47784649; (c) Clifton Ladd, C.W.B., some rights reserved (CC BY); https://www.inaturalist.org/photos/47784649; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Bigtooth Maple', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/bigtooth_maple_inat_630701291_w960_q80_64bd8318bcba.webp', 'Acer grandidentatum', 'Tree', 'iNaturalist Photo 630701291; (c) Shaun Case, some rights reserved (CC BY); https://www.inaturalist.org/photos/630701291; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Bigtooth Maple', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/bigtooth_maple_inat_169423277_w960_q80_b0d69b20a2de.webp', 'Acer grandidentatum', 'Tree', 'iNaturalist Photo 169423277; (c) Jo Roberts, some rights reserved (CC BY); https://www.inaturalist.org/photos/169423277; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 40. Red Maple
            Trees('Red Maple', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/red_maple_inat_54219880_w960_q80_245b7a04f875.webp', 'Acer rubrum', 'Tree', 'iNaturalist Photo 54219880; (c) Tom Norton, some rights reserved (CC BY); https://www.inaturalist.org/photos/54219880; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Red Maple', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/red_maple_inat_120949606_w960_q80_2826da30892e.webp', 'Acer rubrum', 'Tree', 'iNaturalist Photo 120949606; (c) Michael J. Papay, some rights reserved (CC BY); https://www.inaturalist.org/photos/120949606; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Red Maple', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/red_maple_inat_618504222_w960_q80_7180f943da5e.webp', 'Acer rubrum', 'Tree', 'iNaturalist Photo 618504222; (c) Michael Nerrie, some rights reserved (CC BY); https://www.inaturalist.org/photos/618504222; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 41. Mexican Buckeye
            Trees('Mexican Buckeye', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/mexican_buckeye_inat_450665953_w960_q80_41c46f7f903b.webp', 'Ungnadia speciosa', 'Tree', 'iNaturalist Photo 450665953; (c) Tom Field, some rights reserved (CC BY); https://www.inaturalist.org/photos/450665953; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Mexican Buckeye', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/mexican_buckeye_inat_375258843_w960_q80_c19b590066cd.webp', 'Ungnadia speciosa', 'Tree', 'iNaturalist Photo 375258843; CC0; observer: lanechaffin; https://www.inaturalist.org/photos/375258843; CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Mexican Buckeye', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/mexican_buckeye_inat_53884481_w960_q80_791256dc2051.webp', 'Ungnadia speciosa', 'Tree', 'iNaturalist Photo 53884481; (c) Barbara S. Shirley, some rights reserved (CC BY); https://www.inaturalist.org/photos/53884481; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 42. Carolina Basswood
            Trees('Carolina Basswood', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/carolina_basswood_inat_261759846_w960_q80_4cc2b570de33.webp', 'Tilia americana var. caroliniana', 'Tree', 'iNaturalist Photo 261759846; (c) Kristály Cravens-Liszak, some rights reserved (CC BY); https://www.inaturalist.org/photos/261759846; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Carolina Basswood', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/carolina_basswood_inat_373486428_w960_q80_3870f7907299.webp', 'Tilia americana var. caroliniana', 'Tree', 'iNaturalist Photo 373486428; CC0; observer: mikoikoi; https://www.inaturalist.org/photos/373486428; CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Carolina Basswood', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/carolina_basswood_inat_130043589_w960_q80_f7b488f4bae0.webp', 'Tilia americana var. caroliniana', 'Tree', 'iNaturalist Photo 130043589; (c) Will McFarland, some rights reserved (CC BY); https://www.inaturalist.org/photos/130043589; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # 43. Rusty Blackhaw
            Trees("Rusty Blackhaw", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/Rusty+BlackhawFull.jpg", "Viburnum rufidulum", "Tree", "Photo 64043896, (c) Sam Kieschnick", ""),
            Trees("Rusty Blackhaw", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/Rusty+BlackhawLeaf.jpg", "Viburnum rufidulum", "Tree", "Photo 358268337, (c) Libby Aragon", ""),
            Trees("Rusty Blackhaw", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/Rusty+BlackhawBark.jpeg", "Viburnum rufidulum", "Tree", "Photo 118435303, (c) Michelle W.", ""),

            # # 44. Two-wing Silverbell
            Trees('Two-wing Silverbell', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/two-wing_silverbell_inat_184898469_w960_q80_99e9a44f95b7.webp', 'Halesia diptera', 'Tree', 'iNaturalist Photo 184898469; (c) Daniel Patterson, some rights reserved (CC BY); https://www.inaturalist.org/photos/184898469; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Two-wing Silverbell', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/two-wing_silverbell_inat_119612355_w960_q80_b662a5185e1a.webp', 'Halesia diptera', 'Tree', 'iNaturalist Photo 119612355; (c) Michelle W. （鍾偉瑋）, some rights reserved (CC BY); https://www.inaturalist.org/photos/119612355; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Two-wing Silverbell', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/two-wing_silverbell_inat_1653812_w960_q80_69b6572b56aa.webp', 'Halesia diptera', 'Tree', 'iNaturalist Photo 1653812; (c) Laura Clark, some rights reserved (CC BY); https://www.inaturalist.org/photos/1653812; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 45. Flowering Dogwood
            Trees('Flowering Dogwood', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/flowering_dogwood_inat_488913924_w960_q80_c43ca2bcc7b5.webp', 'Cornus florida', 'Tree', 'iNaturalist Photo 488913924; (c) florawhite, some rights reserved (CC BY); https://www.inaturalist.org/photos/488913924; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Flowering Dogwood', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/flowering_dogwood_inat_400080409_w960_q80_b12d35e19b98.webp', 'Cornus florida', 'Tree', 'iNaturalist Photo 400080409; (c) M. Whitson, some rights reserved (CC BY); https://www.inaturalist.org/photos/400080409; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Flowering Dogwood', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/flowering_dogwood_inat_27773168_w960_q80_40c8d3d04e3f.webp', 'Cornus florida', 'Tree', 'iNaturalist Photo 27773168; (c) Ron Burkert, some rights reserved (CC BY); https://www.inaturalist.org/photos/27773168; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 46. Longleaf Pine
            Trees('Longleaf Pine', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/longleaf_pine_inat_119146722_w960_q80_77df63c716e6.webp', 'Pinus palustris', 'Tree', 'iNaturalist Photo 119146722; CC0; observer: Alan Weakley; https://www.inaturalist.org/photos/119146722; CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Longleaf Pine', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/longleaf_pine_inat_99700219_w960_q80_e2216d1f12ca.webp', 'Pinus palustris', 'Tree', 'iNaturalist Photo 99700219; (c) Jay Horn, some rights reserved (CC BY); https://www.inaturalist.org/photos/99700219; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Longleaf Pine', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/longleaf_pine_inat_119146745_w960_q80_94f01de0631e.webp', 'Pinus palustris', 'Tree', 'iNaturalist Photo 119146745; CC0; observer: Alan Weakley; https://www.inaturalist.org/photos/119146745; CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 47. Shortleaf Pine
            Trees('Shortleaf Pine', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/shortleaf_pine_inat_260245636_w960_q80_4c4c3855a104.webp', 'Pinus echinata', 'Tree', 'iNaturalist Photo 260245636; CC0; observer: Kristi Zoebelein; https://www.inaturalist.org/photos/260245636; CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Shortleaf Pine', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/shortleaf_pine_inat_260245617_w960_q80_b0a0be332601.webp', 'Pinus echinata', 'Tree', 'iNaturalist Photo 260245617; CC0; observer: Kristi Zoebelein; https://www.inaturalist.org/photos/260245617; CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Shortleaf Pine', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/shortleaf_pine_inat_450633370_w960_q80_ee7154f1cb43.webp', 'Pinus echinata', 'Tree', 'iNaturalist Photo 450633370; (c) Scott Cave, some rights reserved (CC BY); https://www.inaturalist.org/photos/450633370; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 48. Overcup Oak
            Trees('Overcup Oak', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/overcup_oak_inat_56957224_w960_q80_7f9a0957255b.webp', 'Quercus lyrata', 'Tree', 'iNaturalist Photo 56957224; (c) Emily Summerbell, some rights reserved (CC BY); https://www.inaturalist.org/photos/56957224; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Overcup Oak', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/overcup_oak_inat_511082677_w960_q80_31f4aebe471c.webp', 'Quercus lyrata', 'Tree', 'iNaturalist Photo 511082677; (c) Anne Parker, some rights reserved (CC BY); https://www.inaturalist.org/photos/511082677; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Overcup Oak', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/overcup_oak_inat_56907402_w960_q80_3ad14f647a0c.webp', 'Quercus lyrata', 'Tree', 'iNaturalist Photo 56907402; (c) Emily Summerbell, some rights reserved (CC BY); https://www.inaturalist.org/photos/56907402; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 49. Water Oak
            Trees('Water Oak', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/water_oak_inat_343785564_w960_q80_55aefc6d8d15.webp', 'Quercus nigra', 'Tree', 'iNaturalist Photo 343785564; CC0; observer: lanechaffin; https://www.inaturalist.org/photos/343785564; CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Water Oak', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/water_oak_inat_86499721_w960_q80_65fbb2704aae.webp', 'Quercus nigra', 'Tree', 'iNaturalist Photo 86499721; (c) Cody Stricker, some rights reserved (CC BY); https://www.inaturalist.org/photos/86499721; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Water Oak', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/water_oak_inat_452603003_w960_q80_2cd47aa6dba8.webp', 'Quercus nigra', 'Tree', 'iNaturalist Photo 452603003; (c) Texas Bird Family, some rights reserved (CC BY); https://www.inaturalist.org/photos/452603003; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 50. Willow Oak
            Trees('Willow Oak', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/willow_oak_inat_364939950_w960_q80_07e7e809c793.webp', 'Quercus phellos', 'Tree', 'iNaturalist Photo 364939950; (c) Anne Parker, some rights reserved (CC BY); https://www.inaturalist.org/photos/364939950; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Willow Oak', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/willow_oak_inat_649406371_w960_q80_fa879c5f9b3f.webp', 'Quercus phellos', 'Tree', 'iNaturalist Photo 649406371; (c) Elissa Totin, some rights reserved (CC BY); https://www.inaturalist.org/photos/649406371; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Willow Oak', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/willow_oak_inat_364939879_w960_q80_b29d0319b565.webp', 'Quercus phellos', 'Tree', 'iNaturalist Photo 364939879; (c) Anne Parker, some rights reserved (CC BY); https://www.inaturalist.org/photos/364939879; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 51. American Elm
            Trees('American Elm', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/american_elm_inat_458352812_w960_q80_c401d3c9e5e8.webp', 'Ulmus americana', 'Tree', 'iNaturalist Photo 458352812; (c) Ben Redding, some rights reserved (CC BY); https://www.inaturalist.org/photos/458352812; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('American Elm', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/american_elm_inat_517298255_w960_q80_bcfecfca52d7.webp', 'Ulmus americana', 'Tree', 'iNaturalist Photo 517298255; CC0; observer: Ben Sims; https://www.inaturalist.org/photos/517298255; CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('American Elm', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/american_elm_inat_257645875_w960_q80_90a2556f44d2.webp', 'Ulmus americana', 'Tree', 'iNaturalist Photo 257645875; (c) Sandy Wolkenberg, some rights reserved (CC BY); https://www.inaturalist.org/photos/257645875; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 52. Winged Elm
            Trees('Winged Elm', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/winged_elm_inat_453257473_w960_q80_c7d8be701d7a.webp', 'Ulmus alata', 'Tree', 'iNaturalist Photo 453257473; CC0; observer: lanechaffin; https://www.inaturalist.org/photos/453257473; CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Winged Elm', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/winged_elm_inat_126092633_w960_q80_e2a57918ff7d.webp', 'Ulmus alata', 'Tree', 'iNaturalist Photo 126092633; (c) Brand R, some rights reserved (CC BY); https://www.inaturalist.org/photos/126092633; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Winged Elm', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/winged_elm_inat_135092063_w960_q80_510fe7d6b5a7.webp', 'Ulmus alata', 'Tree', 'iNaturalist Photo 135092063; (c) Michael J. Papay, some rights reserved (CC BY); https://www.inaturalist.org/photos/135092063; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # 53. Black Cherry
            Trees("Black Cherry", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/Black+CherryFull.jpg", "Prunus serotina", "Tree", "Photo 64562125, (c) Emily Summerbell", ""),
            Trees("Black Cherry", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/Black+CherryLeaf.jpg", "Prunus serotina", "Tree", "Photo 18479136, (c) Laura Clark", ""),
            Trees("Black Cherry", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/Black+CherryBark.jpg", "Prunus serotina", "Tree", "Photo 618804717, (c) Northcut", ""),

            # # 54. Carolina Buckthorn
            Trees('Carolina Buckthorn', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/carolina_buckthorn_inat_370878052_w960_q80_bdf405be67a5.webp', 'Frangula caroliniana', 'Tree', 'iNaturalist Photo 370878052; (c) Daniel Patterson, some rights reserved (CC BY); https://www.inaturalist.org/photos/370878052; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Carolina Buckthorn', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/carolina_buckthorn_inat_402442474_w960_q80_bd0648487669.webp', 'Frangula caroliniana', 'Tree', 'iNaturalist Photo 402442474; (c) Daniel Patterson, some rights reserved (CC BY); https://www.inaturalist.org/photos/402442474; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Carolina Buckthorn', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/carolina_buckthorn_inat_224579032_w960_q80_7470fad972b9.webp', 'Frangula caroliniana', 'Tree', 'iNaturalist Photo 224579032; (c) Jeff Wilson, some rights reserved (CC BY); https://www.inaturalist.org/photos/224579032; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 55. Common Buttonbush
            Trees('Common Buttonbush', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/common_buttonbush_inat_84064913_w960_q80_55aa434f0277.webp', 'Cephalanthus occidentalis', 'Tree', 'iNaturalist Photo 84064913; CC0; observer: Adam Kranz; https://www.inaturalist.org/photos/84064913; CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Common Buttonbush', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/common_buttonbush_inat_100658823_w960_q80_dbc512c6ddcf.webp', 'Cephalanthus occidentalis', 'Tree', 'iNaturalist Photo 100658823; (c) Evelyn Davis, some rights reserved (CC BY); https://www.inaturalist.org/photos/100658823; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Common Buttonbush', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/common_buttonbush_inat_253433251_w960_q80_d145fb364dc5.webp', 'Cephalanthus occidentalis', 'Tree', 'iNaturalist Photo 253433251; (c) Adrienne van den Beemt, some rights reserved (CC BY); https://www.inaturalist.org/photos/253433251; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 56. Green Ash
            Trees('Green Ash', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/green_ash_inat_216766944_w960_q80_d80110c03e93.webp', 'Fraxinus pennsylvanica', 'Tree', 'iNaturalist Photo 216766944; CC0; observer: Allan Harris; https://www.inaturalist.org/photos/216766944; CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Green Ash', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/green_ash_inat_148436336_w960_q80_c8ef7ddfbbc4.webp', 'Fraxinus pennsylvanica', 'Tree', 'iNaturalist Photo 148436336; CC0; observer: Vince La Tassa; https://www.inaturalist.org/photos/148436336; CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Green Ash', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/green_ash_inat_38353477_w960_q80_65bcb3e444a4.webp', 'Fraxinus pennsylvanica', 'Tree', 'iNaturalist Photo 38353477; (c) Wendelyn Bolles, some rights reserved (CC BY); https://www.inaturalist.org/photos/38353477; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 57. White Ash
            Trees('White Ash', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/white_ash_inat_86549068_w960_q80_e52032f45c05.webp', 'Fraxinus americana', 'Tree', 'iNaturalist Photo 86549068; CC0; observer: Jim Bennett; https://www.inaturalist.org/photos/86549068; CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('White Ash', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/white_ash_inat_10521926_w960_q80_d8b37d8d79ba.webp', 'Fraxinus americana', 'Tree', 'iNaturalist Photo 10521926; CC0; observer: Tom Rogers; https://www.inaturalist.org/photos/10521926; CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('White Ash', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/white_ash_inat_37423559_w960_q80_b64c0ad00b50.webp', 'Fraxinus americana', 'Tree', 'iNaturalist Photo 37423559; (c) Wendelyn Bolles, some rights reserved (CC BY); https://www.inaturalist.org/photos/37423559; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # # 58. Texas Mulberry
            Trees('Texas Mulberry', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/texas_mulberry_inat_392907293_w960_q80_1e75f0b918d7.webp', 'Morus microphylla', 'Tree', 'iNaturalist Photo 392907293; CC0; observer: Katherine McElveen; https://www.inaturalist.org/photos/392907293; CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Texas Mulberry', 'leaf', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/texas_mulberry_inat_21268701_w960_q80_2fb24867fe73.webp', 'Morus microphylla', 'Tree', 'iNaturalist Photo 21268701; (c) Sam Kieschnick, some rights reserved (CC BY); https://www.inaturalist.org/photos/21268701; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Trees('Texas Mulberry', 'bark', 'https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/texas_mulberry_inat_152495484_w960_q80_99f64c0b1ffc.webp', 'Morus microphylla', 'Tree', 'iNaturalist Photo 152495484; (c) Alison Northup, some rights reserved (CC BY); https://www.inaturalist.org/photos/152495484; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),

            # 59. Red Mulberry
            Trees("Red Mulberry", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/Red+MulberryFull.jpg", "Morus rubra", "Tree", "Photo 186577373, (c) Sam Kieschnick", ""),
            Trees("Red Mulberry", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/Red+MulberryLeaf.jpeg", "Morus rubra", "Tree", "Photo 371438844, (c) Mike Tilley", ""),
            Trees("Red Mulberry", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/Red+MulberryBark.jpg", "Morus rubra", "Tree", "Photo 93803054, (c) Brand R", ""),

            # 60. Sassafras
            Trees("Sassafras", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/close_fullsize/SassafrasFull.jpg", "Sassafras albidum", "Tree", "Photo 167737857, (c) Northcut", ""),
            Trees("Sassafras", "leaf", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/leaf/SassafrasLeaf.jpeg", "Sassafras albidum", "Tree", "Photo 194523029, (c) Reid Hardin", ""),
            Trees("Sassafras", "bark", "https://texasplants.s3.us-east-2.amazonaws.com/texas_trees/bark/SassafrasBark.jpg", "Sassafras albidum", "Tree", "Photo 167472690, (c) Sandy Wolkenberg", ""),
        ]

        # bouncer loop for trees -- checking both plant_name AND image_type (leaf/bark/close)
        # Updated bouncer loop for trees -- now updates URLs if they changed!
        for tree in trees:
            exists = Trees.query.filter_by(plant_name=tree.plant_name, image_type=tree.image_type).first()
            if not exists:
                db.session.add(tree)
            else:
                # Keep image credit and taxonomy in sync with updated images.
                for field in ('image_url', 'source', 'scientific_name', 'plant_type', 'location_counties'):
                    value = getattr(tree, field)
                    if value and getattr(exists, field) != value:
                        setattr(exists, field, value)

        # --- FLOWERS (Top 15) ---
        flowers = [
            Flowers("Texas Bluebonnet", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/flowers/Texas+Bluebonnet.jpeg", "Lupinus texensis", "Flower", "Photo 264945809, (c) Wes Copas", ""),
            Flowers("Firewheel", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/flowers/Firewheel.jpg", "Gaillardia pulchella", "Flower", "Photo 288364229, (c) Jay Pruett", ""),
            Flowers("Pinkladies", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/flowers/Pinkladies.jpeg", "Oenothera speciosa", "Flower", "Photo 322034089, (c) W Rao", ""),
            Flowers("Black-eyed Susan", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/flowers/Black-eyed+Susan.jpeg", "Rudbeckia hirta", "Flower", "Photo 46212572, (c) Andrew St. Paul", ""),
            Flowers("Prairie Coneflower", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/flowers/Prairie+Coneflower.jpg", "Ratibida columnifera", "Flower", "Photo 655594917, (c) Linda Jo Conn", ""),
            Flowers("Texas Paintbrush", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/flowers/Texas+Paintbrush.jpeg", "Castilleja indivisa", "Flower", "Photo 493119223, (c) davis0117", ""),
            Flowers("Plains Coreopsis", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/flowers/Plains+Coreopsis.jpg", "Coreopsis tinctoria", "Flower", "Photo 651421381, (c) Texas Bird Family", ""),
            Flowers("Drummond Phlox", "close_fullsize", "https://texasplants.s3.us-east-2.amazonaws.com/flowers/Drummond+Phlox.jpg", "Phlox drummondii", "Flower", "Photo 67915786, (c) Kyle M. Simpson", ""),
            Flowers('Texas Bluebell', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/flowers/texas_bluebell_inat_75148296_w960_q80_3a01d4a7c639.webp', 'Eustoma exaltatum', 'Flower', 'iNaturalist Photo 75148296; CC0; observer: Cecelia Alexander; https://www.inaturalist.org/photos/75148296; CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Flowers('Purple Coneflower', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/flowers/purple_coneflower_inat_154207793_w960_q80_767b097c1211.webp', 'Echinacea purpurea', 'Flower', 'iNaturalist Photo 154207793; CC0; observer: Jason Swanson; https://www.inaturalist.org/photos/154207793; CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Flowers('Common Sunflower', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/flowers/common_sunflower_inat_155296308_w960_q80_f6fbfb7e2264.webp', 'Helianthus annuus', 'Flower', 'iNaturalist Photo 155296308; (c) Jay Pruett, some rights reserved (CC BY); https://www.inaturalist.org/photos/155296308; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Flowers('Winecup', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/flowers/winecup_inat_126971109_w960_q80_1c21afe20109.webp', 'Callirhoe involucrata', 'Flower', 'iNaturalist Photo 126971109; (c) Megan Kossa, some rights reserved (CC BY); https://www.inaturalist.org/photos/126971109; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Flowers('Texas Lantana', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/flowers/texas_lantana_inat_664267787_w960_q80_6d3f3d12d094.webp', 'Lantana urticoides', 'Flower', 'iNaturalist Photo 664267787; (c) Ian McFaul, some rights reserved (CC BY); https://www.inaturalist.org/photos/664267787; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Flowers('Standing Cypress', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/flowers/standing_cypress_inat_680420195_w960_q80_df35fd9304f8.webp', 'Ipomopsis rubra', 'Flower', 'iNaturalist Photo 680420195; (c) Holly Bonorden Jentsch, some rights reserved (CC BY); https://www.inaturalist.org/photos/680420195; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
            Flowers('Blue-eyed Grass', 'close_fullsize', 'https://texasplants.s3.us-east-2.amazonaws.com/flowers/blue-eyed_grass_inat_3798402_w960_q80_e23211cc0325.webp', 'Sisyrinchium campestre', 'Flower', 'iNaturalist Photo 3798402; (c) aarongunnar, some rights reserved (CC BY); https://www.inaturalist.org/photos/3798402; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/; resized to maximum 960px and converted to WebP (quality 80); no crop', ''),
        ]
        
        for flower in flowers:
            exists = Flowers.query.filter_by(plant_name=flower.plant_name).first()
            if not exists:
                db.session.add(flower)
            else:
                for field in ('image_url', 'source', 'scientific_name', 'plant_type', 'location_counties'):
                    value = getattr(flower, field)
                    if value and getattr(exists, field) != value:
                        setattr(exists, field, value)

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
