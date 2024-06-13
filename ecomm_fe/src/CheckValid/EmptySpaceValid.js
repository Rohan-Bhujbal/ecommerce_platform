const EmptySpaceFieldValid = (e) => {
    if (e.target.value.length === 0 && e.which === 32) {
       return e.preventDefault();
    };
}

export default EmptySpaceFieldValid;