import React from "react";
import { Pagination } from "react-pagination-bar";
import 'react-pagination-bar/dist/index.css';

const CommonPagination = (props) => {
    const { currentPage, paginationLength, currentFunction } = props;
    return(<div className="paginationCustom">
        <Pagination
            currentPage={currentPage}
            itemsPerPage={parseInt(paginationLength.record_limit)}
            onPageChange={(pageNumber) => currentFunction(pageNumber)}
            totalItems={parseInt(paginationLength.total_records)}
            pageNeighbours={2}
        />
    </div>)
}

export default CommonPagination;