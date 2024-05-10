export default class Building {
  constructor(sqft) {
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  evacuationWarningMessage() {
    if (this.constructor !== Building
        && this.evacuationWarningMessage === undefined) {
      throw new TypeError('Class extending Building must override evacuationWarningMessage');
    }
  }
}
