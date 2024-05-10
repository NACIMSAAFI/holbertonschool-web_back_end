export default class Building {
  constructor(sqft) {
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  evacuationWarningMessage() {
    if (!this.evacuationWarningMessage) {
      throw new TypeError('Class extending Building must override evacuationWarningMessage');
    }
  }
}
