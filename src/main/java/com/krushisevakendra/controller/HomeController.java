package com.krushisevakendra.controller;

import com.krushisevakendra.dto.FertilizerCalcDto;
import com.krushisevakendra.entity.Category;
import com.krushisevakendra.entity.Feedback;
import com.krushisevakendra.entity.Product;
import com.krushisevakendra.entity.User;
import com.krushisevakendra.exception.ResourceNotFoundException;
import com.krushisevakendra.repository.FeedbackRepository;
import com.krushisevakendra.repository.OfferRepository;
import com.krushisevakendra.security.SecurityUtil;
import com.krushisevakendra.service.CategoryService;
import com.krushisevakendra.service.FarmingService;
import com.krushisevakendra.service.ProductService;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@Controller
public class HomeController {

    private final ProductService productService;
    private final CategoryService categoryService;
    private final FarmingService farmingService;
    private final OfferRepository offerRepository;
    private final FeedbackRepository feedbackRepository;
    private final SecurityUtil securityUtil;

    @org.springframework.beans.factory.annotation.Value("${app.shop.name}") private String shopName;
    @org.springframework.beans.factory.annotation.Value("${app.shop.address}") private String shopAddress;
    @org.springframework.beans.factory.annotation.Value("${app.shop.mobile}") private String shopMobile;
    @org.springframework.beans.factory.annotation.Value("${app.shop.email}") private String shopEmail;
    @org.springframework.beans.factory.annotation.Value("${app.shop.gstin}") private String shopGstin;
    @org.springframework.beans.factory.annotation.Value("${app.shop.opening-hours}") private String shopHours;
    @org.springframework.beans.factory.annotation.Value("${app.shop.map-url}") private String shopMapUrl;
    @org.springframework.beans.factory.annotation.Value("${app.shop.map-embed-url}") private String shopMapEmbedUrl;

    public HomeController(ProductService productService,
                          CategoryService categoryService,
                          FarmingService farmingService,
                          OfferRepository offerRepository,
                          FeedbackRepository feedbackRepository,
                          SecurityUtil securityUtil) {
        this.productService = productService;
        this.categoryService = categoryService;
        this.farmingService = farmingService;
        this.offerRepository = offerRepository;
        this.feedbackRepository = feedbackRepository;
        this.securityUtil = securityUtil;
    }

    @GetMapping({"/", "/home"})
    public String home(Model model) {
        model.addAttribute("categories", categoryService.getAllActiveCategories());
        model.addAttribute("featuredProducts", productService.getFeaturedProducts());
        model.addAttribute("offers", offerRepository.findByActiveTrueOrderByCreatedAtDesc());
        model.addAttribute("farmingTips", farmingService.getCropCareTips());
        model.addAttribute("weather", farmingService.getWeatherForecast("Chhatrapati Sambhajinagar"));
        model.addAttribute("shopName", shopName);
        model.addAttribute("shopAddress", shopAddress);
        model.addAttribute("shopMobile", shopMobile);
        model.addAttribute("shopEmail", shopEmail);
        model.addAttribute("shopGstin", shopGstin);
        model.addAttribute("shopHours", shopHours);
        model.addAttribute("shopMapUrl", shopMapUrl);
        model.addAttribute("shopMapEmbedUrl", shopMapEmbedUrl);
        return "public/index";
    }

    @GetMapping("/products")
    public String productCatalog(
            @RequestParam(required = false) Long categoryId,
            @RequestParam(required = false) String company,
            @RequestParam(required = false) Double minPrice,
            @RequestParam(required = false) Double maxPrice,
            @RequestParam(required = false, defaultValue = "false") boolean inStockOnly,
            @RequestParam(required = false) String keyword,
            @RequestParam(required = false, defaultValue = "newest") String sort,
            @RequestParam(required = false, defaultValue = "0") int page,
            @RequestParam(required = false, defaultValue = "12") int size,
            Model model) {

        Sort sorting = switch (sort) {
            case "price_asc" -> Sort.by("price").ascending();
            case "price_desc" -> Sort.by("price").descending();
            case "rating" -> Sort.by("rating").descending();
            case "popular" -> Sort.by("reviewCount").descending();
            default -> Sort.by("createdAt").descending();
        };

        Page<Product> productPage = productService.searchAndFilter(
                categoryId, company, minPrice, maxPrice, inStockOnly, keyword,
                PageRequest.of(page, size, sorting)
        );

        model.addAttribute("productPage", productPage);
        model.addAttribute("categories", categoryService.getAllActiveCategories());
        model.addAttribute("brands", productService.getAllBrands());
        model.addAttribute("selectedCategory", categoryId);
        model.addAttribute("selectedCompany", company);
        model.addAttribute("minPrice", minPrice);
        model.addAttribute("maxPrice", maxPrice);
        model.addAttribute("inStockOnly", inStockOnly);
        model.addAttribute("keyword", keyword);
        model.addAttribute("currentSort", sort);

        return "public/products";
    }

    @GetMapping("/products/{id}")
    public String productDetails(@PathVariable Long id, Model model) {
        Product product = productService.getProductById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Product not found with id: " + id));

        List<Feedback> reviews = feedbackRepository.findByProductIdAndStatusOrderByCreatedAtDesc(id, "APPROVED");
        List<Product> relatedProducts = productService.getProductsByCategory(product.getCategory().getId());

        model.addAttribute("product", product);
        model.addAttribute("reviews", reviews);
        model.addAttribute("relatedProducts", relatedProducts);
        model.addAttribute("isLoggedIn", securityUtil.isAuthenticated());
        return "public/product-details";
    }

    @PostMapping("/products/{id}/review")
    public String addProductReview(
            @PathVariable Long id,
            @RequestParam Integer rating,
            @RequestParam String review) {

        Optional<User> currentUser = securityUtil.getCurrentUser();
        if (currentUser.isPresent()) {
            Product product = productService.getProductById(id)
                    .orElseThrow(() -> new ResourceNotFoundException("Product not found with id: " + id));

            Feedback fb = new Feedback(currentUser.get(), product, rating, review);
            feedbackRepository.save(fb);

            // Update product rating average
            Double avg = feedbackRepository.calculateAverageRatingForProduct(id);
            long count = feedbackRepository.countApprovedByProductId(id);
            if (avg != null) {
                product.setRating(java.math.BigDecimal.valueOf(avg).setScale(1, java.math.RoundingMode.HALF_UP));
                product.setReviewCount((int) count);
                productService.saveProduct(null); // triggers repository save logic or direct save
            }
        }
        return "redirect:/products/" + id + "?reviewed=true";
    }

    @GetMapping("/offers")
    public String offers(Model model) {
        model.addAttribute("offers", offerRepository.findByActiveTrueOrderByCreatedAtDesc());
        return "public/offers";
    }

    @GetMapping("/farming-tips")
    public String farmingTips(Model model) {
        model.addAttribute("cropCareTips", farmingService.getCropCareTips());
        model.addAttribute("pestTips", farmingService.getPestManagementTips());
        return "public/farming-tips";
    }

    @GetMapping("/weather")
    public String weather(@RequestParam(required = false, defaultValue = "Sangli") String city, Model model) {
        model.addAttribute("weather", farmingService.getWeatherForecast(city));
        model.addAttribute("selectedCity", city);
        return "public/weather";
    }

    @GetMapping("/fertilizer-calculator")
    public String fertilizerCalculator(
            @RequestParam(required = false, defaultValue = "sugarcane") String crop,
            @RequestParam(required = false, defaultValue = "1.0") Double acres,
            @RequestParam(required = false, defaultValue = "Medium Black") String soilType,
            @RequestParam(required = false, defaultValue = "Full Season") String stage,
            Model model) {

        FertilizerCalcDto calculation = farmingService.calculateFertilizer(crop, acres, soilType, stage);
        model.addAttribute("calc", calculation);
        return "public/fertilizer-calc";
    }

    @GetMapping("/about")
    public String about() {
        return "public/about";
    }

    @GetMapping("/contact")
    public String contact(Model model) {
        model.addAttribute("shopName", shopName);
        model.addAttribute("shopAddress", shopAddress);
        model.addAttribute("shopMobile", shopMobile);
        model.addAttribute("shopEmail", shopEmail);
        model.addAttribute("shopGstin", shopGstin);
        model.addAttribute("shopHours", shopHours);
        model.addAttribute("shopMapUrl", shopMapUrl);
        model.addAttribute("shopMapEmbedUrl", shopMapEmbedUrl);
        return "public/contact";
    }

    @GetMapping("/faq")
    public String faq() {
        return "public/faq";
    }
}
