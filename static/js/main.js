// Variables
const custOne = document.getElementById('sheet-one');
const custTwo = document.getElementById('sheet-two');
const custThree = document.getElementById('sheet-three');
const custFour = document.getElementById('sheet-four');
const custBtn1 = document.getElementById('cust-btn-1');
const custBtn2 = document.getElementById('cust-btn-2');
const custBtn3 = document.getElementById('cust-btn-3');
const custBtn4 = document.getElementById('cust-btn-4');
const highDayBtn = document.getElementById('high-day-btn');
const highNightBtn = document.getElementById('high-night-btn');
const highEnergyBtn = document.getElementById('high-energy-cost-btn');
const highDayRate = document.getElementById('highest-day-rate');
const highNightRate = document.getElementById('highest-night-rate');
const highEnergyCost = document.getElementById('highest-energy-cost');

// Customer One button
$(custBtn1).click(function() {
    $(custOne).css('display', 'block');
    $(custTwo,custThree,custFour).css('display', 'none');
    $(custThree).css('display', 'none');
    $(custFour).css('display', 'none');
    $(highDayRate).css('display', 'none');
    $(highNightRate).css('display', 'none');
    $(highEnergyCost).css('display', 'none');
});

// Customer Two button
$(custBtn2).click(function() {
    $(custTwo).css('display', 'block');
    $(custOne).css('display', 'none');
    $(custThree).css('display', 'none');
    $(custFour).css('display', 'none');
    $(highDayRate).css('display', 'none');
    $(highNightRate).css('display', 'none');
    $(highEnergyCost).css('display', 'none');
});

// Customer Three button
$(custBtn3).click(function() {
    $(custThree).css('display', 'block');
    $(custOne).css('display', 'none');
    $(custTwo).css('display', 'none');
    $(custFour).css('display', 'none');
    $(highDayRate).css('display', 'none');
    $(highNightRate).css('display', 'none');
    $(highEnergyCost).css('display', 'none');
});

// Customer Four button
$(custBtn4).click(function() {
    $(custFour).css('display', 'block');
    $(custOne).css('display', 'none');
    $(custTwo).css('display', 'none');
    $(custThree).css('display', 'none');
    $(highDayRate).css('display', 'none');
    $(highNightRate).css('display', 'none');
    $(highEnergyCost).css('display', 'none');
});

// Highest Day Rate
$(highDayBtn).click(function() {
    $(highDayRate).css('display', 'block');
    $(highNightRate).css('display', 'none');
    $(highEnergyCost).css('display', 'none');
    $(custFour).css('display', 'none');
    $(custOne).css('display', 'none');
    $(custTwo).css('display', 'none');
    $(custThree).css('display', 'none');
});

// Highest Night Rate
$(highNightBtn).click(function() {
    $(highNightRate).css('display', 'block');
    $(highDayRate).css('display', 'none');
    $(highEnergyCost).css('display', 'none');
    $(custFour).css('display', 'none');
    $(custOne).css('display', 'none');
    $(custTwo).css('display', 'none');
    $(custThree).css('display', 'none');
});

// Highest Energy Cost
$(highEnergyBtn).click(function() {
    $(highEnergyCost).css('display', 'block');
    $(highDayRate).css('display', 'none');
    $(highNightRate).css('display', 'none');
    $(custFour).css('display', 'none');
    $(custOne).css('display', 'none');
    $(custTwo).css('display', 'none');
    $(custThree).css('display', 'none');
});