export interface Laptop {
	id: number;
	manufacturer: string;
	model_name: string;
	category: string;
	screen_diag: number;
	screen_res: string;
	screen_type: string;
	screen_touch: string;
	cpu_vendor: string;
	cpu: string;
	ram: number;
	storage: number;
	storage_type: string;
	gpu_vendor: string;
	gpu: string;
	os: string;
	os_version: string;
	mass: number;
	price: number;
}

export interface Ranges {
	screen_diag: [number, number];
	ram: [number, number];
	storage: [number, number];
	mass: [number, number];
	price: [number, number];
}

export interface Checkboxes {
	manufacturer: string[];
	category: string[];
	screen_res: string[];
	screen_touch: string[];
	cpu_vendor: string[];
	storage_type: string[];
	os: string[];
}

export interface Filter {
	checkboxes: Checkboxes;
	ranges: Ranges;
}

export type SearchBoxes = { [checkbox: string]: string[] };
export type SearchRanges = { [range: string]: [number, number] };
export type SearchWords = string;
