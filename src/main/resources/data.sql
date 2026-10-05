-- ===================================================================
-- 🌱 KRUSHI SEVA KENDRA - SAMPLE & DEMO SEED DATA
-- ===================================================================

-- 1. Insert Roles
INSERT INTO roles (id, name) VALUES 
(1, 'ROLE_ADMIN'),
(2, 'ROLE_CUSTOMER');

-- 2. Insert Users (BCrypt encoded passwords for '$2a$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy' -> 'password123' / 'admin123')
-- Passwords will also be automatically hashed on startup by DataInitializer if needed.
INSERT INTO users (id, name, mobile, email, address, village, taluka, district, password_hash, status, created_at) VALUES
(1, 'Dattatray Kulkarni (Admin)', '9876543210', 'admin@krushiseva.com', 'Shop No. 12, APMC Market', 'Sangli', 'Miraj', 'Sangli', '$2a$10$wEkgz1uWp3E7q8lE/KqGVOl5B55H6wXo/OaAevgB6qjYy7jGomU1y', 'ACTIVE', NOW()),
(2, 'Ramesh Patil (Farmer)', '9822012345', 'ramesh@patil.com', 'Near Gram Panchayat, Post Kasbe Digraj', 'Kasbe Digraj', 'Miraj', 'Sangli', '$2a$10$wEkgz1uWp3E7q8lE/KqGVOl5B55H6wXo/OaAevgB6qjYy7jGomU1y', 'ACTIVE', NOW()),
(3, 'Suresh Deshmukh (Farmer)', '9822054321', 'suresh@deshmukh.com', 'Gat No. 45, Near Sugar Factory', 'Walwa', 'Islampur', 'Sangli', '$2a$10$wEkgz1uWp3E7q8lE/KqGVOl5B55H6wXo/OaAevgB6qjYy7jGomU1y', 'ACTIVE', NOW()),
(4, 'Ananda Jadhav (Farmer)', '9822098765', 'ananda@jadhav.com', 'Vikaswadi, Post Shirala', 'Shirala', 'Shirala', 'Sangli', '$2a$10$wEkgz1uWp3E7q8lE/KqGVOl5B55H6wXo/OaAevgB6qjYy7jGomU1y', 'ACTIVE', NOW());

-- Map User Roles
INSERT INTO user_roles (user_id, role_id) VALUES
(1, 1), -- Admin
(2, 2), -- Customer
(3, 2), -- Customer
(4, 2); -- Customer

-- 3. Insert Product Categories
INSERT INTO categories (id, name, name_mr, description, image, status) VALUES
(1, 'Seeds', 'बियाणे', 'High yield certified hybrid and organic seeds for crops, vegetables, and pulses.', 'seeds.jpg', 'ACTIVE'),
(2, 'Fertilizers', 'खते', 'Chemical, water-soluble, NPK and micronutrient fertilizers for balanced soil nutrition.', 'fertilizers.jpg', 'ACTIVE'),
(3, 'Pesticides', 'कीटकनाशके', 'Broad-spectrum insecticides, fungicides, and weedicides for crop protection.', 'pesticides.jpg', 'ACTIVE'),
(4, 'Farming Tools', 'शेती अवजारे', 'Manual, battery sprayers, pruning shears, tarpaulins and agricultural hand tools.', 'tools.jpg', 'ACTIVE'),
(5, 'Drip Irrigation', 'ठिबक सिंचन', 'Drip laterals, drippers, screen filters, venturi injectors and PVC fittings.', 'irrigation.jpg', 'ACTIVE'),
(6, 'Animal Feed', 'पशुखाद्य', 'Nutritious cattle feed pellets, mineral mixtures, and dairy nutritional supplements.', 'animalfeed.jpg', 'ACTIVE'),
(7, 'Organic Products', 'सेंद्रिय उत्पादने', 'Neem cake, vermicompost, bio-fertilizers, and organic bio-stimulants.', 'organic.jpg', 'ACTIVE'),
(8, 'Plant Growth Promoters', 'वाढ संप्रेरके', 'Humic acid, seaweed extract, gibberellic acid and flowering enhancers.', 'growth.jpg', 'ACTIVE');

-- 4. Insert Comprehensive Realistic Agricultural Products (12 Products)
INSERT INTO products (id, category_id, name, name_mr, company, sku, barcode, price, discount_price, gst_rate, description, usage_instructions, image, stock_quantity, minimum_stock, batch_number, expiry_date, rating, review_count, status) VALUES
(1, 1, 'Mahyco Bollgard II Cotton Seeds (475g)', 'माहिको बीजी-२ कापूस बियाणे', 'Mahyco Seeds', 'MAH-COT-01', '890123456701', 864.00, 820.00, 0.00, 'High quality certified Bollgard II cotton seed pack with refuge seeds for bollworm resistance and high yield.', 'Sow at 4x1.5 feet spacing during onset of monsoon. Treat with bio-fungicide if necessary.', 'cotton_seeds.jpg', 65, 10, 'BCH-2026-COT1', '2027-04-30', 4.8, 12, 'ACTIVE'),

(2, 1, 'JS 335 Certified Soybean Seeds (30 Kg)', 'जेएस ३३५ प्रमाणित सोयाबीन बियाणे', 'Mahabeej', 'MBJ-SOY-335', '890123456702', 2850.00, 2700.00, 0.00, 'High germination certified soybean seeds suitable for heavy and medium black soils with high oil content.', 'Sowing rate: 30 kg per acre. Treat with Rhizobium and Trichoderma before sowing.', 'soybean_seeds.jpg', 40, 8, 'BCH-2026-SOY2', '2027-03-31', 4.7, 9, 'ACTIVE'),

(3, 2, 'Mahadhan 24:24:0 NPK Granular Fertilizer (50 Kg)', 'महाधन २४:२४:० खत (५० किलो)', 'Deepak Fertilisers', 'MAH-NPK-24', '890123456703', 1750.00, 1680.00, 5.00, 'Complex ammonium phosphate fertilizer providing essential Nitrogen and Phosphorus for rapid root establishment and tillering.', 'Apply as basal or top dressing: 1 to 2 bags per acre depending on soil test report.', 'fertilizer_npk.jpg', 90, 15, 'BCH-2026-NPK3', '2028-12-31', 4.9, 21, 'ACTIVE'),

(4, 2, 'IFFCO Neem Coated Urea (45 Kg)', 'इफको नीम कोटेड युरिया (४५ किलो)', 'IFFCO Ltd.', 'IFF-UREA-45', '890123456704', 266.50, 266.50, 5.00, 'Neem-coated slow release nitrogen fertilizer for vegetative growth and green foliage across all crops.', 'Apply in split doses after weeding and irrigation to prevent leaching.', 'urea_bag.jpg', 150, 25, 'BCH-2026-UREA4', '2029-01-01', 4.9, 34, 'ACTIVE'),

(5, 2, 'Coromandel Gromor 10:26:26 Complex (50 Kg)', 'कोरोमंडल ग्रोमोर १०:२६:२६ खत', 'Coromandel International', 'COR-GRO-1026', '890123456705', 1820.00, 1750.00, 5.00, 'High potash and phosphorus balanced fertilizer ideal for sugarcane, cotton, banana, and vegetables for fruit development.', 'Basal application: 2 bags per acre during soil preparation or side placement.', 'gromor_bag.jpg', 80, 12, 'BCH-2026-GRO5', '2028-10-15', 4.8, 16, 'ACTIVE'),

(6, 3, 'Syngenta Ampligo 150 ZC Insecticide (200 ml)', 'सिंजेन्टा अँप्लिगो कीटकनाशक (२०० मिली)', 'Syngenta India', 'SYN-AMP-200', '890123456706', 950.00, 890.00, 18.00, 'Broad-spectrum insecticide for controlling Fall Armyworm, bollworms, stem borers and caterpillars.', 'Dose: 0.5 to 0.7 ml per liter of water (100 ml per acre). Spray during early pest infestation.', 'ampligo.jpg', 35, 5, 'BCH-2026-AMP6', '2027-09-30', 4.9, 18, 'ACTIVE'),

(7, 3, 'Tata Rallis Rogor Insecticide - Dimethoate 30% EC (1 Litre)', 'टाटा रॅलीस रोगोर कीटकनाशक (१ लिटर)', 'Tata Rallis India', 'TAT-ROG-1L', '890123456707', 620.00, 575.00, 18.00, 'Effective systemic insecticide and acaricide against sucking pests like aphids, thrips, jassids, and mites.', 'Mix 1.5 ml to 2 ml per liter of water. Ensure thorough coverage on the underside of leaves.', 'rogor.jpg', 50, 8, 'BCH-2026-ROG7', '2027-11-20', 4.6, 14, 'ACTIVE'),

(8, 4, 'Falcon 16 Litre 12V-12Ah Battery Operated Sprayer', 'फाल्कन १६ लिटर बॅटरी पंप', 'Falcon Agri', 'FAL-SPY-16L', '890123456708', 3200.00, 2850.00, 12.00, 'Heavy duty double motor battery knapsack sprayer with brass lance, regulator, and multi-nozzle set.', 'Charge for 6 hours before initial use. Flush with clean water after spraying chemicals.', 'battery_sprayer.jpg', 18, 3, 'BCH-2026-SPY8', '2030-01-01', 4.8, 27, 'ACTIVE'),

(9, 5, 'Jain Irrigation 16mm Drip Lateral Inline Pipe (400 Meters)', 'जैन ठिबक १६ मिमी लॅटरल पाईप (४०० मीटर)', 'Jain Irrigation Systems', 'JAI-DRP-16M', '890123456709', 3600.00, 3350.00, 12.00, 'ISI certified Class-II virgin polymer drip lateral with 40 cm dripper spacing and 4 LPH discharge rate.', 'Lay along crop rows. Flush mainlines before installing end plugs. Maintain 1 to 1.5 kg/cm2 pressure.', 'drip_pipe.jpg', 22, 4, 'BCH-2026-DRP9', '2032-12-31', 4.9, 15, 'ACTIVE'),

(10, 6, 'Godrej Cattle Feed Super Pellet (50 Kg)', 'गोदरेज दुग्धपशू खाद्य सुपर पेंड', 'Godrej Agrovet', 'GOD-CAT-50', '890123456710', 1450.00, 1380.00, 5.00, 'High protein (22%) and balanced fat cattle feed for improving milk yield and animal health in dairy cows & buffaloes.', 'Feed 400g feed per liter of milk produced plus 1.5 kg for body maintenance daily.', 'cattle_feed.jpg', 60, 10, 'BCH-2026-CAT10', '2026-12-31', 4.7, 19, 'ACTIVE'),

(11, 7, 'Green Harvest Pure Neem Cake Powder (25 Kg)', 'ग्रीन हार्वेस्ट सेंद्रिय निंबोळी पेंड (२५ किलो)', 'Green Harvest Bio', 'GRN-NEEM-25', '890123456711', 850.00, 780.00, 5.00, '100% natural cold pressed neem cake enriched with azadirachtin to control root nematodes and termite attacks.', 'Broadcast 100 to 150 kg per acre during field preparation or around root zone of fruit trees.', 'neem_cake.jpg', 45, 6, 'BCH-2026-NEEM11', '2027-08-31', 4.8, 11, 'ACTIVE'),

(12, 8, 'Bayer Planofix Plant Growth Regulator (100 ml)', 'बायर प्लॅनोफिक्स वाढ संप्रेरक (१०० मिली)', 'Bayer CropScience', 'BAY-PLA-100', '890123456712', 170.00, 155.00, 18.00, 'Alpha Naphthyl Acetic Acid (NAA 4.5% SL) solution for reducing premature flower, square and fruit dropping.', 'Mix 1 ml in 4.5 liters of water. Spray during peak flowering and fruit development stage.', 'planofix.jpg', 75, 12, 'BCH-2026-PLA12', '2028-04-30', 4.9, 23, 'ACTIVE');

-- 5. Insert Sample Orders
INSERT INTO orders (id, order_number, user_id, subtotal, discount, gst, total, payment_method, payment_status, order_status, delivery_address, notes, created_at) VALUES
(1, 'KSK-2026-00001', 2, 4380.00, 100.00, 219.00, 4499.00, 'UDHARI', 'PENDING', 'DELIVERED', 'Kasbe Digraj, Taluka Miraj, Dist Sangli - 416305', 'Deliver to field near well pump', '2026-08-01 10:30:00'),
(2, 'KSK-2026-00002', 3, 2850.00, 0.00, 342.00, 3192.00, 'UPI', 'PAID', 'DELIVERED', 'Gat No 45, Walwa, Dist Sangli', 'Paid via PhonePe UPI QR', '2026-08-05 14:15:00'),
(3, 'KSK-2026-00003', 2, 1750.00, 50.00, 87.50, 1787.50, 'CASH', 'PAID', 'PROCESSING', 'Kasbe Digraj, Sangli', 'Direct counter purchase pickup', '2026-08-12 11:00:00');

-- 6. Insert Sample Order Items
INSERT INTO order_items (id, order_id, product_id, quantity, price, gst, total) VALUES
(1, 1, 2, 1, 2700.00, 0.00, 2700.00),
(2, 1, 3, 1, 1680.00, 84.00, 1764.00),
(3, 2, 8, 1, 2850.00, 342.00, 3192.00),
(4, 3, 5, 1, 1750.00, 87.50, 1837.50);

-- 7. Insert Udhari (Credit) Ledger Records
INSERT INTO udhari (id, user_id, order_id, total_amount, paid_amount, remaining_amount, due_date, status, created_at, updated_at) VALUES
(1, 2, 1, 5000.00, 2500.00, 2500.00, '2026-08-25', 'ACTIVE', '2026-08-01 10:30:00', '2026-08-10 16:00:00'),
(2, 4, NULL, 3500.00, 1000.00, 2500.00, '2026-08-15', 'OVERDUE', '2026-07-20 09:00:00', '2026-08-02 11:30:00');

-- 8. Insert Payments
INSERT INTO payments (id, user_id, udhari_id, order_id, amount, payment_method, transaction_id, payment_date, remarks) VALUES
(1, 2, 1, 1, 2500.00, 'UPI', 'UPI-TXN-982201092837', '2026-08-10 16:00:00', 'Part payment received via Google Pay'),
(2, 3, NULL, 2, 3192.00, 'UPI', 'UPI-TXN-881726354412', '2026-08-05 14:16:00', 'Full order payment via UPI QR'),
(3, 4, 2, NULL, 1000.00, 'CASH', 'CASH-REC-00102', '2026-08-02 11:30:00', 'Cash received at shop counter');

-- 9. Insert Notifications
INSERT INTO notifications (id, user_id, title, message, type, is_read, sent_at) VALUES
(1, 2, 'Udhari Payment Reminder', 'Dear Ramesh Patil, your outstanding Udhari balance is ₹2,500.00 due on 25 August 2026. Please pay on time. Thank you!', 'WHATSAPP', FALSE, '2026-08-15 09:00:00'),
(2, 2, 'Order Confirmed', 'Your order KSK-2026-00001 for ₹4,499.00 has been confirmed and delivered.', 'IN_APP', TRUE, '2026-08-01 11:00:00'),
(3, 4, 'Overdue Udhari Notice', 'Dear Ananda Jadhav, your Udhari payment of ₹2,500.00 was due on 15 August 2026 and is now overdue. Kindly clear at earliest.', 'SMS', FALSE, '2026-08-16 10:00:00'),
(4, 3, 'New Monsoon Season Offer', 'Get 10% instant discount on all Organic Bio-fertilizers this week! Use code KHARIF10 at checkout.', 'IN_APP', FALSE, '2026-08-14 08:30:00');

-- 10. Insert Offers & Coupons
INSERT INTO offers (id, title, description, discount_type, discount_value, coupon_code, min_order_amount, start_date, end_date, active) VALUES
(1, 'Kharif Special 10% Discount', 'Special discount for Kharif season crop protection and bio-fertilizers.', 'PERCENTAGE', 10.00, 'KHARIF10', 1000.00, '2026-06-01', '2026-09-30', TRUE),
(2, 'Flat ₹150 Off on Seeds & Fertilizers', 'Flat discount on orders above ₹3,000 across all seed and fertilizer categories.', 'FIXED', 150.00, 'FARMER150', 3000.00, '2026-08-01', '2026-10-31', TRUE),
(3, 'Drip Irrigation Festive Mega Offer', 'Get ₹300 off on bulk drip lateral bundles above ₹5,000.', 'FIXED', 300.00, 'DRIP300', 5000.00, '2026-08-10', '2026-11-30', TRUE);

-- 11. Insert Sample Feedback & Reviews
INSERT INTO feedback (id, user_id, product_id, rating, review, status, created_at) VALUES
(1, 2, 1, 5, 'उत्कृष्ट उगवण क्षमता आणि बोंडअळीचा कसलाही प्रादुर्भाव नाही. खूप चांगले बियाणे!', 'APPROVED', '2026-08-10 14:00:00'),
(2, 3, 3, 5, 'महाधन २४:२४:० मुळे उसाची फुटवे आणि वाढ खूप जोमदार झाली. रास्त भाव मिळाला.', 'APPROVED', '2026-08-08 12:30:00'),
(3, 4, 8, 4, 'फाल्कन बॅटरी पंप खूप चांगला चालतो, एकदा चार्जिंग केल्यावर २५ पंप आरामात फवारणी होते.', 'APPROVED', '2026-08-06 18:00:00');
