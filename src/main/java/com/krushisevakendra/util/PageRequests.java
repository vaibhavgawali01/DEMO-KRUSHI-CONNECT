package com.krushisevakendra.util;

import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;

public final class PageRequests {

    private static final int MAX_PAGE_SIZE = 100;

    private PageRequests() {
    }

    public static Pageable bounded(int page, int size) {
        return bounded(page, size, Sort.unsorted());
    }

    public static Pageable bounded(int page, int size, Sort sort) {
        return PageRequest.of(Math.max(0, page), Math.max(1, Math.min(size, MAX_PAGE_SIZE)), sort);
    }
}
