package com.krushisevakendra.config;

import com.krushisevakendra.entity.*;
import com.krushisevakendra.enums.*;
import com.krushisevakendra.repository.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

@Component
public class DataInitializer implements CommandLineRunner {

    private static final Logger log = LoggerFactory.getLogger(DataInitializer.class);

    private final RoleRepository roleRepository;
    private final UserRepository userRepository;
    private final CategoryRepository categoryRepository;
    private final ProductRepository productRepository;
    private final OrderRepository orderRepository;
    private final UdhariRepository udhariRepository;
    private final PaymentRepository paymentRepository;
    private final NotificationRepository notificationRepository;
    private final OfferRepository offerRepository;
    private final FeedbackRepository feedbackRepository;
    private final PasswordEncoder passwordEncoder;

    public DataInitializer(RoleRepository roleRepository,
                           UserRepository userRepository,
                           CategoryRepository categoryRepository,
                           ProductRepository productRepository,
                           OrderRepository orderRepository,
                           UdhariRepository udhariRepository,
                           PaymentRepository paymentRepository,
                           NotificationRepository notificationRepository,
                           OfferRepository offerRepository,
                           FeedbackRepository feedbackRepository,
                           PasswordEncoder passwordEncoder) {
        this.roleRepository = roleRepository;
        this.userRepository = userRepository;
        this.categoryRepository = categoryRepository;
        this.productRepository = productRepository;
        this.orderRepository = orderRepository;
        this.udhariRepository = udhariRepository;
        this.paymentRepository = paymentRepository;
        this.notificationRepository = notificationRepository;
        this.offerRepository = offerRepository;
        this.feedbackRepository = feedbackRepository;
        this.passwordEncoder = passwordEncoder;
    }

    @Override
    @Transactional
    public void run(String... args) {
        log.info("Initializing Krushi Seva Kendra Application Data...");

        // 1. Initialize Roles
        Role adminRole = roleRepository.findByName(RoleName.ROLE_ADMIN)
                .orElseGet(() -> roleRepository.save(new Role(RoleName.ROLE_ADMIN)));

        Role customerRole = roleRepository.findByName(RoleName.ROLE_CUSTOMER)
                .orElseGet(() -> roleRepository.save(new Role(RoleName.ROLE_CUSTOMER)));

        // 2. Initialize Users (Admin & Sample Farmers)
        User admin = userRepository.findByEmail("admin@krushiseva.com").orElseGet(() -> {
            User u = new User();
            u.setName("Dattatray Kulkarni (Admin)");
            u.setMobile("9876543210");
            u.setEmail("admin@krushiseva.com");
            u.setAddress("Shop No. 12, APMC Market Yard, Sangli");
            u.setVillage("Sangli");
            u.setTaluka("Miraj");
            u.setDistrict("Sangli");
            u.setPasswordHash(passwordEncoder.encode("admin123"));
            u.setStatus("ACTIVE");
            u.setCreatedAt(LocalDateTime.now());
            Set<Role> roles = new HashSet<>();
            roles.add(adminRole);
            roles.add(customerRole);
            u.setRoles(roles);
            return userRepository.save(u);
        });

        // Always guarantee ROLE_ADMIN and active status for admin
        if (admin != null) {
            boolean hasAdmin = admin.getRoles().stream().anyMatch(r -> r.getName() == RoleName.ROLE_ADMIN);
            if (!hasAdmin) {
                admin.getRoles().add(adminRole);
                admin.getRoles().add(customerRole);
                admin.setPasswordHash(passwordEncoder.encode("admin123"));
                admin.setStatus("ACTIVE");
                userRepository.save(admin);
                log.info("Guaranteed ROLE_ADMIN on admin user: {}", admin.getEmail());
            }
        }

        userRepository.findByMobile("9876543210").ifPresent(u -> {
            boolean hasAdmin = u.getRoles().stream().anyMatch(r -> r.getName() == RoleName.ROLE_ADMIN);
            if (!hasAdmin) {
                u.getRoles().add(adminRole);
                u.setPasswordHash(passwordEncoder.encode("admin123"));
                u.setStatus("ACTIVE");
                userRepository.save(u);
                log.info("Guaranteed ROLE_ADMIN on 9876543210");
            }
        });

        User ramesh = userRepository.findByEmail("ramesh@patil.com").orElseGet(() -> {
            User u = new User();
            u.setName("Ramesh Patil");
            u.setMobile("9822012345");
            u.setEmail("ramesh@patil.com");
            u.setAddress("Near Gram Panchayat, Post Kasbe Digraj");
            u.setVillage("Kasbe Digraj");
            u.setTaluka("Miraj");
            u.setDistrict("Sangli");
            u.setPasswordHash(passwordEncoder.encode("farmer123"));
            u.setStatus("ACTIVE");
            u.setCreatedAt(LocalDateTime.now());
            u.setRoles(Collections.singleton(customerRole));
            return userRepository.save(u);
        });

        User suresh = userRepository.findByEmail("suresh@deshmukh.com").orElseGet(() -> {
            User u = new User();
            u.setName("Suresh Deshmukh");
            u.setMobile("9822054321");
            u.setEmail("suresh@deshmukh.com");
            u.setAddress("Gat No. 45, Near Sugar Factory");
            u.setVillage("Walwa");
            u.setTaluka("Islampur");
            u.setDistrict("Sangli");
            u.setPasswordHash(passwordEncoder.encode("farmer123"));
            u.setStatus("ACTIVE");
            u.setCreatedAt(LocalDateTime.now());
            u.setRoles(Collections.singleton(customerRole));
            return userRepository.save(u);
        });

        // 3. Initialize Categories
        if (categoryRepository.count() == 0) {
            Category catSeeds = categoryRepository.save(new Category("Seeds", "बियाणे", "High yield certified hybrid and organic crop seeds.", "seeds.jpg"));
            Category catFert = categoryRepository.save(new Category("Fertilizers", "खते", "Chemical, water-soluble, NPK and micronutrient fertilizers.", "fertilizers.jpg"));
            Category catPest = categoryRepository.save(new Category("Pesticides", "कीटकनाशके", "Broad-spectrum insecticides, fungicides, and weedicides.", "pesticides.jpg"));
            Category catTools = categoryRepository.save(new Category("Farming Tools", "शेती अवजारे", "Battery sprayers, pruning shears, tarpaulins and hand tools.", "tools.jpg"));
            Category catDrip = categoryRepository.save(new Category("Drip Irrigation", "ठिबक सिंचन", "Drip laterals, drippers, screen filters and fittings.", "irrigation.jpg"));
            Category catFeed = categoryRepository.save(new Category("Animal Feed", "पशुखाद्य", "Cattle feed pellets, mineral mixtures and supplements.", "animalfeed.jpg"));
            Category catOrganic = categoryRepository.save(new Category("Organic Products", "सेंद्रिय उत्पादने", "Neem cake, vermicompost and organic bio-stimulants.", "organic.jpg"));
            Category catGrowth = categoryRepository.save(new Category("Plant Growth Promoters", "वाढ संप्रेरके", "Humic acid, seaweed extract and flowering boosters.", "growth.jpg"));

            // 4. Initialize Products
            Product p1 = createProduct(catSeeds, "Mahyco Bollgard II Cotton Seeds (475g)", "माहिको बीजी-२ कापूस बियाणे", "Mahyco Seeds",
                    "MAH-COT-01", "890123456701", new BigDecimal("864.00"), new BigDecimal("820.00"), BigDecimal.ZERO,
                    "High quality certified Bollgard II cotton seed pack with refuge seeds for bollworm resistance and high yield.",
                    "Sow at 4x1.5 feet spacing during onset of monsoon. Treat with bio-fungicide if necessary.",
                    "cotton_seeds.jpg", 65, 10, "BCH-2026-COT1", LocalDate.now().plusMonths(10));

            Product p2 = createProduct(catSeeds, "JS 335 Certified Soybean Seeds (30 Kg)", "जेएस ३३५ प्रमाणित सोयाबीन बियाणे", "Mahabeej",
                    "MBJ-SOY-335", "890123456702", new BigDecimal("2850.00"), new BigDecimal("2700.00"), BigDecimal.ZERO,
                    "High germination certified soybean seeds suitable for heavy and medium black soils with high oil content.",
                    "Sowing rate: 30 kg per acre. Treat with Rhizobium and Trichoderma before sowing.",
                    "soybean_seeds.jpg", 40, 8, "BCH-2026-SOY2", LocalDate.now().plusMonths(8));

            Product p3 = createProduct(catFert, "Mahadhan 24:24:0 NPK Granular Fertilizer (50 Kg)", "महाधन २४:२४:० खत (५० किलो)", "Deepak Fertilisers",
                    "MAH-NPK-24", "890123456703", new BigDecimal("1750.00"), new BigDecimal("1680.00"), new BigDecimal("5.00"),
                    "Complex ammonium phosphate fertilizer providing essential Nitrogen and Phosphorus for rapid root establishment.",
                    "Apply as basal or top dressing: 1 to 2 bags per acre depending on soil test report.",
                    "fertilizer_npk.jpg", 90, 15, "BCH-2026-NPK3", LocalDate.now().plusYears(2));

            Product p4 = createProduct(catFert, "IFFCO Neem Coated Urea (45 Kg)", "इफको नीम कोटेड युरिया (४५ किलो)", "IFFCO Ltd.",
                    "IFF-UREA-45", "890123456704", new BigDecimal("266.50"), new BigDecimal("266.50"), new BigDecimal("5.00"),
                    "Neem-coated slow release nitrogen fertilizer for vegetative growth and green foliage across all crops.",
                    "Apply in split doses after weeding and irrigation to prevent leaching.",
                    "urea_bag.jpg", 150, 25, "BCH-2026-UREA4", LocalDate.now().plusYears(3));

            Product p5 = createProduct(catFert, "Coromandel Gromor 10:26:26 Complex (50 Kg)", "कोरोमंडल ग्रोमोर १०:२६:२६ खत", "Coromandel International",
                    "COR-GRO-1026", "890123456705", new BigDecimal("1820.00"), new BigDecimal("1750.00"), new BigDecimal("5.00"),
                    "High potash and phosphorus balanced fertilizer ideal for sugarcane, cotton, banana, and vegetables.",
                    "Basal application: 2 bags per acre during soil preparation or side placement.",
                    "gromor_bag.jpg", 80, 12, "BCH-2026-GRO5", LocalDate.now().plusYears(2));

            Product p6 = createProduct(catPest, "Syngenta Ampligo 150 ZC Insecticide (200 ml)", "सिंजेन्टा अँप्लिगो कीटकनाशक (२०० मिली)", "Syngenta India",
                    "SYN-AMP-200", "890123456706", new BigDecimal("950.00"), new BigDecimal("890.00"), new BigDecimal("18.00"),
                    "Broad-spectrum insecticide for controlling Fall Armyworm, bollworms, stem borers and caterpillars.",
                    "Dose: 0.5 to 0.7 ml per liter of water (100 ml per acre). Spray during early pest infestation.",
                    "ampligo.jpg", 35, 5, "BCH-2026-AMP6", LocalDate.now().plusMonths(14));

            Product p7 = createProduct(catPest, "Tata Rallis Rogor Insecticide - Dimethoate 30% EC (1 Litre)", "टाटा रॅलीस रोगोर कीटकनाशक (१ लिटर)", "Tata Rallis India",
                    "TAT-ROG-1L", "890123456707", new BigDecimal("620.00"), new BigDecimal("575.00"), new BigDecimal("18.00"),
                    "Effective systemic insecticide and acaricide against sucking pests like aphids, thrips, and mites.",
                    "Mix 1.5 ml to 2 ml per liter of water. Ensure thorough coverage on the underside of leaves.",
                    "rogor.jpg", 50, 8, "BCH-2026-ROG7", LocalDate.now().plusMonths(18));

            Product p8 = createProduct(catTools, "Falcon 16 Litre 12V-12Ah Battery Operated Sprayer", "फाल्कन १६ लिटर बॅटरी पंप", "Falcon Agri",
                    "FAL-SPY-16L", "890123456708", new BigDecimal("3200.00"), new BigDecimal("2850.00"), new BigDecimal("12.00"),
                    "Heavy duty double motor battery knapsack sprayer with brass lance, regulator, and multi-nozzle set.",
                    "Charge for 6 hours before initial use. Flush with clean water after spraying chemicals.",
                    "battery_sprayer.jpg", 18, 3, "BCH-2026-SPY8", LocalDate.now().plusYears(4));

            Product p9 = createProduct(catDrip, "Jain Irrigation 16mm Drip Lateral Inline Pipe (400 Meters)", "जैन ठिबक १६ मिमी लॅटरल पाईप (४०० मीटर)", "Jain Irrigation Systems",
                    "JAI-DRP-16M", "890123456709", new BigDecimal("3600.00"), new BigDecimal("3350.00"), new BigDecimal("12.00"),
                    "ISI certified Class-II virgin polymer drip lateral with 40 cm dripper spacing and 4 LPH discharge rate.",
                    "Lay along crop rows. Flush mainlines before installing end plugs. Maintain 1 to 1.5 kg/cm2 pressure.",
                    "drip_pipe.jpg", 22, 4, "BCH-2026-DRP9", LocalDate.now().plusYears(5));

            Product p10 = createProduct(catFeed, "Godrej Cattle Feed Super Pellet (50 Kg)", "गोदरेज दुग्धपशू खाद्य सुपर पेंड", "Godrej Agrovet",
                    "GOD-CAT-50", "890123456710", new BigDecimal("1450.00"), new BigDecimal("1380.00"), new BigDecimal("5.00"),
                    "High protein (22%) and balanced fat cattle feed for improving milk yield and animal health.",
                    "Feed 400g feed per liter of milk produced plus 1.5 kg for body maintenance daily.",
                    "cattle_feed.jpg", 60, 10, "BCH-2026-CAT10", LocalDate.now().plusMonths(6));

            Product p11 = createProduct(catOrganic, "Green Harvest Pure Neem Cake Powder (25 Kg)", "ग्रीन हार्वेस्ट सेंद्रिय निंबोळी पेंड (२५ किलो)", "Green Harvest Bio",
                    "GRN-NEEM-25", "890123456711", new BigDecimal("850.00"), new BigDecimal("780.00"), new BigDecimal("5.00"),
                    "100% natural cold pressed neem cake enriched with azadirachtin to control root nematodes and termites.",
                    "Broadcast 100 to 150 kg per acre during field preparation or around root zone of fruit trees.",
                    "neem_cake.jpg", 45, 6, "BCH-2026-NEEM11", LocalDate.now().plusMonths(12));

            Product p12 = createProduct(catGrowth, "Bayer Planofix Plant Growth Regulator (100 ml)", "बायर प्लॅनोफिक्स वाढ संप्रेरक (१०० मिली)", "Bayer CropScience",
                    "BAY-PLA-100", "890123456712", new BigDecimal("170.00"), new BigDecimal("155.00"), new BigDecimal("18.00"),
                    "Alpha Naphthyl Acetic Acid (NAA 4.5% SL) solution for reducing premature flower and fruit dropping.",
                    "Mix 1 ml in 4.5 liters of water. Spray during peak flowering and fruit development stage.",
                    "planofix.jpg", 75, 12, "BCH-2026-PLA12", LocalDate.now().plusYears(2));

            // 5. Initialize Offers
            Offer off1 = new Offer();
            off1.setTitle("Kharif Special 10% Discount");
            off1.setDescription("Special seasonal discount on bio-fertilizers and crop protectors.");
            off1.setDiscountType("PERCENTAGE");
            off1.setDiscountValue(new BigDecimal("10.00"));
            off1.setCouponCode("KHARIF10");
            off1.setMinOrderAmount(new BigDecimal("1000.00"));
            off1.setStartDate(LocalDate.now().minusDays(10));
            off1.setEndDate(LocalDate.now().plusMonths(3));
            off1.setActive(true);
            offerRepository.save(off1);

            Offer off2 = new Offer();
            off2.setTitle("Flat ₹150 Off on Seeds & Fertilizers");
            off2.setDescription("Flat discount on orders above ₹3,000 across all farming inputs.");
            off2.setDiscountType("FIXED");
            off2.setDiscountValue(new BigDecimal("150.00"));
            off2.setCouponCode("FARMER150");
            off2.setMinOrderAmount(new BigDecimal("3000.00"));
            off2.setStartDate(LocalDate.now().minusDays(5));
            off2.setEndDate(LocalDate.now().plusMonths(2));
            off2.setActive(true);
            offerRepository.save(off2);

            // 6. Initialize Sample Order & Udhari Records
            Order o1 = new Order();
            o1.setOrderNumber("KSK-2026-00001");
            o1.setUser(ramesh);
            o1.setSubtotal(new BigDecimal("4380.00"));
            o1.setDiscount(new BigDecimal("100.00"));
            o1.setGst(new BigDecimal("219.00"));
            o1.setTotal(new BigDecimal("4499.00"));
            o1.setPaymentMethod(PaymentMethod.UDHARI);
            o1.setPaymentStatus(PaymentStatus.PENDING);
            o1.setOrderStatus(OrderStatus.DELIVERED);
            o1.setDeliveryAddress("Kasbe Digraj, Taluka Miraj, Dist Sangli - 416305");
            o1.setNotes("Deliver near well pump");
            o1.setCreatedAt(LocalDateTime.now().minusDays(18));
            orderRepository.save(o1);

            OrderItem item1 = new OrderItem(o1, p2, 1, new BigDecimal("2700.00"), BigDecimal.ZERO, new BigDecimal("2700.00"));
            OrderItem item2 = new OrderItem(o1, p3, 1, new BigDecimal("1680.00"), new BigDecimal("84.00"), new BigDecimal("1764.00"));
            o1.addOrderItem(item1);
            o1.addOrderItem(item2);
            orderRepository.save(o1);

            // Udhari account for Ramesh
            Udhari udhari1 = new Udhari(ramesh, o1, new BigDecimal("5000.00"), LocalDate.now().plusDays(10));
            udhari1.setPaidAmount(new BigDecimal("2500.00"));
            udhari1.setRemainingAmount(new BigDecimal("2500.00"));
            udhari1.setStatus(UdhariStatus.ACTIVE);
            udhari1.setCreatedAt(LocalDateTime.now().minusDays(18));
            udhariRepository.save(udhari1);

            // Partial payment recorded for Ramesh
            Payment pay1 = new Payment(ramesh, udhari1, o1, new BigDecimal("2500.00"), PaymentMethod.UPI, "UPI-TXN-982201092837", "Part payment via PhonePe");
            pay1.setPaymentDate(LocalDateTime.now().minusDays(8));
            paymentRepository.save(pay1);

            // Overdue Udhari account for Suresh
            Udhari udhari2 = new Udhari(suresh, null, new BigDecimal("3500.00"), LocalDate.now().minusDays(5));
            udhari2.setPaidAmount(new BigDecimal("1000.00"));
            udhari2.setRemainingAmount(new BigDecimal("2500.00"));
            udhari2.setStatus(UdhariStatus.OVERDUE);
            udhari2.setCreatedAt(LocalDateTime.now().minusDays(35));
            udhariRepository.save(udhari2);

            // Feedback / Reviews
            feedbackRepository.save(new Feedback(ramesh, p1, 5, "उत्कृष्ट उगवण क्षमता आणि बोंडअळीचा कसलाही प्रादुर्भाव नाही. खूप चांगले बियाणे!"));
            feedbackRepository.save(new Feedback(suresh, p3, 5, "महाधन २४:२४:० मुळे उसाची फुटवे आणि वाढ खूप जोमदार झाली. रास्त भाव मिळाला."));

            // Notifications
            Notification notif1 = new Notification(ramesh, "Udhari Payment Reminder",
                    "Dear Ramesh Patil, your outstanding Udhari balance is ₹2,500.00 due on " + udhari1.getDueDate() + ". Please pay on time. Thank you!",
                    NotificationType.WHATSAPP);
            notificationRepository.save(notif1);

            log.info("Krushi Seva Kendra seed data initialized successfully!");
        }
    }

    private Product createProduct(Category category, String name, String nameMr, String company,
                                  String sku, String barcode, BigDecimal price, BigDecimal discountPrice,
                                  BigDecimal gstRate, String desc, String usage, String image,
                                  int stock, int minStock, String batch, LocalDate expiry) {
        Product p = new Product();
        p.setCategory(category);
        p.setName(name);
        p.setNameMr(nameMr);
        p.setCompany(company);
        p.setSku(sku);
        p.setBarcode(barcode);
        p.setPrice(price);
        p.setDiscountPrice(discountPrice);
        p.setGstRate(gstRate);
        p.setDescription(desc);
        p.setUsageInstructions(usage);
        p.setImage(image);
        p.setStockQuantity(stock);
        p.setMinimumStock(minStock);
        p.setBatchNumber(batch);
        p.setExpiryDate(expiry);
        p.setStatus("ACTIVE");
        p.setCreatedAt(LocalDateTime.now());
        p.setUpdatedAt(LocalDateTime.now());
        return productRepository.save(p);
    }
}
